# 🚀 Repo-GPT

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/pranesh-2005/Repo-GPT?style=social)](https://github.com/pranesh-2005/Repo-GPT)
[![GitHub forks](https://img.shields.io/github/forks/pranesh-2005/Repo-GPT?style=social)](https://github.com/pranesh-2005/Repo-GPT/network)
[![Open Issues](https://img.shields.io/github/issues/pranesh-2005/Repo-GPT)](https://github.com/pranesh-2005/Repo-GPT/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## 📖 Introduction

**Repo-GPT** is an intelligent GitHub repository analysis tool that leverages AI to help you understand any codebase instantly! 🔍✨

With Repo-GPT, you can chat with any public GitHub repository and get instant answers about its structure, functionality, and implementation details. Powered by advanced AI models through OpenRouter, Repo-GPT transforms how developers explore and understand codebases.

## ✨ Features

- 🧠 **AI-Powered Code Analysis** - Get intelligent insights about any repository
- 💬 **Natural Language Queries** - Ask questions in plain English about the codebase
- 🌐 **GitHub Integration** - Clone and analyze any public repository
- 🎨 **Beautiful UI** - Clean, modern interface built with Gradio
- 📱 **Responsive Design** - Works great on desktop and mobile
- ⚡ **Fast & Efficient** - Quick analysis with optimized processing
- 🔒 **Secure** - Local processing with environment variable protection
- 🌍 **PWA Support** - Install as a Progressive Web App

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Git
- OpenRouter API Key ([Get one here](https://openrouter.ai/))

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pranesh-2005/Repo-GPT.git
   cd Repo-GPT
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:7860`

## 🚀 Usage

### Basic Usage

1. **Start the Application**
   - Run `python app.py`
   - The Gradio interface will launch automatically

2. **Analyze a Repository**
   - Paste a GitHub repository URL
   - Ask your questions about the codebase
   - Get instant AI-powered insights!

### Example Queries

- "What is the main purpose of this repository?"
- "Explain the key functions in the codebase"
- "How is the project structured?"
- "What are the dependencies used?"
- "Find potential bugs or issues"

### Frontend Setup

For a custom frontend experience:

1. Navigate to the `frontend` directory
2. Serve the static files using any HTTP server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js (if you have it)
   npx serve .
   ```

## 🤝 Contributing

We love contributions! Here's how you can help make Repo-GPT even better:

### Ways to Contribute

- 🐛 **Bug Reports** - Found a bug? Open an issue
- 💡 **Feature Requests** - Have an idea? Let's discuss it
- 🔧 **Code Contributions** - Submit pull requests
- 📚 **Documentation** - Improve docs and examples
- 🧪 **Testing** - Add test cases and improve coverage

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Include type hints where possible
- Write descriptive commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🌟 Support & Star History

If Repo-GPT helps you understand codebases better, please consider:

- ⭐ **Starring the repository** if you find it useful
- 🐛 **Reporting issues** you encounter
- 🤝 **Contributing** to the project
- 📢 **Sharing** with other developers

---

<div align="center">
  <p><strong>Made with ❤️ by the PRANESH</strong></p>
  <p>
    <a href="https://github.com/pranesh-2005/Repo-GPT">⭐ Star us on GitHub ⭐</a>
  </p>
</div>

---


## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Pranesh-2005/Repo-GPT