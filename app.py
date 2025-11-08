import os, shutil, tempfile, re
from pathlib import Path
import gradio as gr
from git import Repo
import requests

# ---------------- CONFIG ----------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = "nvidia/nemotron-nano-12b-v2-vl:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

ALLOWED_EXT = {
    ".py", ".ipynb", ".md", ".txt", ".js", ".ts", ".tsx", ".jsx", ".java",
    ".kt", ".c", ".cpp", ".cs", ".go", ".rs", ".rb", ".php", ".sql", ".html",
    ".css", ".yml", ".yaml", ".toml", ".ini", ".json"
}
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "out", "venv", ".venv",
    "__pycache__", ".next", ".cache", "target", "bin", "obj", ".idea", ".vscode"
}
MAX_FILE_BYTES = 800_000

# ---------------- REPO UTILITIES ----------------
def clone_repo(url: str) -> Path:
    d = Path(tempfile.mkdtemp(prefix=".tmp_repo_")).resolve()
    Repo.clone_from(url, d, depth=1)
    return d

def read_repo_text(repo_dir: Path) -> str:
    buf = []
    for root, dirs, files in os.walk(repo_dir):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in ALLOWED_EXT and p.stat().st_size <= MAX_FILE_BYTES:
                try:
                    txt = p.read_text(encoding="utf-8", errors="ignore")
                    if txt.strip():
                        rel = str(p.relative_to(repo_dir))
                        buf.append(f"\n=== FILE: {rel} ===\n{txt}")
                except Exception:
                    pass
    return "\n".join(buf)

def analyze_repo(url: str):
    if not url or not re.match(r"^https?://", url.strip()):
        return None, "❌ Invalid URL"
    repo_dir = None
    try:
        repo_dir = clone_repo(url.strip())
        text = read_repo_text(repo_dir)
        if not text.strip():
            return None, "⚠️ No readable text files found"
        kb_size = len(text) // 1000
        return text, f"✅ Repo loaded successfully ({kb_size} KB of text)"
    except Exception as e:
        return None, f"❌ Error: {e}"
    finally:
        if repo_dir and Path(repo_dir).exists():
            shutil.rmtree(repo_dir, ignore_errors=True)


# ---------------- OPENROUTER CLIENT ----------------
def openrouter_chat(system_prompt, user_prompt, context=""):
    messages = [{"role": "system", "content": system_prompt}]
    if context:
        messages.append({"role": "system", "content": f"Repository context:\n{context}"})
    messages.append({"role": "user", "content": user_prompt})

    payload = {"model": OPENROUTER_MODEL, "messages": messages}
    try:
        r = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload, timeout=120)
        r.raise_for_status()
        obj = r.json()
        if "choices" in obj and obj["choices"]:
            msg = obj["choices"][0]["message"]["content"]
            return msg.strip()
        return "[OpenRouter] Unexpected response format."
    except Exception as e:
        return f"[OpenRouter error] {e}"
    
# ---------------- CHAT LOGIC ----------------
SYSTEM_PROMPT = (
    "You are an expert developer assistant. You help users explore and understand "
    "a GitHub repository. Base every response strictly on the repo's content and structure. "
    "If unsure, say so. Explain clearly and concisely. Avoid hallucinating."
)

def chat_repo(user_msg, chat_history, repo_text):
    if not repo_text:
        chat_history.append({"role": "assistant", "content": "❌ Please analyze a repository first."})
        return chat_history, ""
    
    context = repo_text[:120000]  # truncate for token safety
    response = openrouter_chat(SYSTEM_PROMPT, user_msg, context)
    chat_history.append({"role": "user", "content": user_msg})
    chat_history.append({"role": "assistant", "content": response})
    return chat_history, ""

# ---------------- GRADIO UI ----------------
with gr.Blocks(title="Repo Chatbot · OpenRouter") as demo:
    gr.Markdown(
        """
        # 🤖 Repo Chatbot — powered by OpenRouter  
        Chat with your GitHub repository!  
        Upload a repo URL and ask anything about its **code, structure, or design**.  
        _(No embeddings, just pure context reasoning.)_
        """
    )

    repo_state = gr.State()
    chat_history = gr.State([])

    with gr.Row():
        repo_url = gr.Textbox(
            label="GitHub repo URL",
            placeholder="https://github.com/owner/repo",
            scale=4
        )
        analyze_btn = gr.Button("🔍 Analyze Repo", scale=1)

    status_box = gr.Markdown()

    # ✅ Add type='messages' to match new format
    chatbot = gr.Chatbot(label="Repo Chatbot", height=500, type="messages")
    user_box = gr.Textbox(label="Ask something about the repo...")

    clear_btn = gr.Button("🧹 Clear Chat")

    # ---- CALLBACKS ----
    def analyze_repo_cb(url):
        text, status = analyze_repo(url)
        return text, status

    analyze_btn.click(analyze_repo_cb, inputs=[repo_url], outputs=[repo_state, status_box])
    user_box.submit(chat_repo, inputs=[user_box, chat_history, repo_state],
                    outputs=[chatbot, user_box])
    clear_btn.click(lambda: ([], ""), None, [chatbot, user_box])

    demo.queue()  # ✅ removed unsupported arg
    demo.launch(server_name="0.0.0.0", server_port=7860)
