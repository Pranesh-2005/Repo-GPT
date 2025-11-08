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
