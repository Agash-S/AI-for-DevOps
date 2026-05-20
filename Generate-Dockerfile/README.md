# 🐳 AI Dockerfile Generator

A GenAI-powered Dockerfile Generator that creates optimized and production-ready Dockerfiles using:

* 🧠 Local LLMs with Ollama
* ☁️ Google Gemini API
* 🐍 Python Automation

This project helps developers generate Dockerfiles quickly while following Docker best practices.

---

# 🚀 Features

✅ Generate Dockerfiles instantly

✅ Supports Local LLM using Ollama

✅ Supports Gemini API

✅ Beginner-friendly setup

✅ Uses Docker best practices

✅ Works from terminal

---

# 🧰 Tech Stack

| Technology | Usage                   |
| ---------- | ----------------------- |
| Python     | Main scripting language |
| Ollama     | Local LLM runtime       |
| LLM Model  | Dockerfile generation   |
| Gemini API | Cloud AI model          |
| Docker     | Containerization        |

---

# 📋 Prerequisites

## 1. Install Python

Download Python from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Verify installation:

```bash
python --version
```

---

# 🧠 Ollama Setup (Local LLM)

## Install Ollama

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### macOS

```bash
brew install ollama
```

### Windows

Download from:

[https://ollama.com/download](https://ollama.com/download)

---

## Start Ollama Service

```bash
ollama serve
```

---

## Pull Llama Model - Size of this model is 5gb and require 8gb ram machine to run smoothly, switch to smaller model if your laptop has low compute, higher the size of the model better the result and consistent output.

```bash
ollama pull huggingface.co/bartowski/qwen2.5-7b-instruct-gguf
```

Alternative models: - Small models

```bash
ollama pull qwen2.5-coder:1.5b
ollama pull llama3.2:1b
```

---

# ☁️ Gemini API Setup

## Generate API Key

Visit:

[https://aistudio.google.com/](https://aistudio.google.com/)

Create a Gemini API Key.

---

## Set Environment Variable

### Linux/macOS

```bash
export GEMINI_API_KEY="your_api_key"
```

### Windows PowerShell

```powershell
setx GEMINI_API_KEY "your_api_key"
```

---

# 📂 Project Structure

```bash
Generate-Dockerfile/
│
├── generate_dockerfile_ollama.py
├── generate_dockerfile_gemini.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Agash-S/AI-for-DevOps.git

cd Generate-Dockerfile
```

---

## Create Virtual Environment

### Linux/macOS

```bash
python3 -m venv LLM
source LLM/bin/activate
```

### Windows

```powershell
python -m venv LLM
.\LLM\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application - It will definitely take some time for low compute machines for Ollama Version.

## Run Ollama Version

```bash
python3 generate_dockerfile_ollama.py
```

---

## Run Gemini Version

```bash
python3 generate_dockerfile_gemini.py
```

---

# 🧪 Example Usage

```bash
Enter programming language: python
Enter programming language: python
# Generated Dockerfile will be displayed...
```

---

# 📦 requirements.txt

```txt
ollama
google.genai
```

---

# 🏆 Troubleshooting

## Ollama Not Running

Start Ollama service:

```bash
ollama serve
```

---

## Model Not Found

```bash
ollama pull #model-name
ollama list
ollama ps
```

---

## Gemini API Errors

Check whether:

* API key is valid
* Environment variable is configured
* Internet connection is available

---

# 🤝 Contributing

Pull requests and contributions are welcome.

Feel free to fork the repository and improve the project.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📝 Share feedback

🚀 Connect on LinkedIn

---

# 📜 License

This project is licensed under the MIT License.
