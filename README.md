# AI Coding Assistant — Mid-Pro Level

An intelligent, locally powered coding assistant built with **LangGraph**, designed to analyze, optimize, and document code using a multi‑agent workflow.  
This project is fully local: **no external APIs, no cloud dependencies, no API keys required**.

---

## 🚀 Features

- **LangGraph Orchestration**  
  Supervisor + 3 specialized agents (Analyzer, Optimizer, DocAgent)

- **Local LLM Support (Qwen, etc.)**  
  Works with local models via your preferred runtime (Ollama, LM Studio, etc.)

- **Code Analysis**  
  Tree‑sitter integration for syntax‑aware inspection

- **Code Quality Tools**  
  - Black (formatting)  
  - Ruff (linting)  
  - Mypy (optional type checking)

- **Zero Cloud Dependencies**  
  100% offline, private, and cost‑free

---

## 📦 Requirements

- Python **3.11+**
- pip (recommended)
- Optional: local LLM runtime (Ollama, LM Studio, etc.)

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ai-coding-assistant

2. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

3. Install dependencies:
pip install -e ".[dev]"

System Architecture:
The assistant follows a sequential multi‑agent workflow:

1. AnalyzerAgent
- Reads input code
- Detects issues, smells, and bad practices
- Produces a structured analysis

2. OptimizerAgent
- Receives original code
- Generates an improved version
- Applies formatting tools (Black)

3. DocAgent
- Generates docstrings, comments, and documentation

4. Supervisor
- Orchestrates the agents
- Manages state
- Produces the final combined output

Usage
- Run the assistant with: python src/main.py --file path/to/your_code.py
Development
- pytest
Format code
- black src/ tests/
Lint
- ruff check src/ tests/
License
- MIT License