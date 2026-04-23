# AI Coding Assistant — Modular Multi‑Agent Architecture

A clean, professional, and fully tested AI Coding Assistant built with a modular multi‑agent architecture.
This project demonstrates engineering best practices, CI/CD automation, and a scalable design suitable for real‑world AI development.

This repository is ideal for recruiters and engineering teams who want to evaluate:

- Code quality
- Architecture design
- Testing discipline
- CI/CD maturity
- Ability to build maintainable AI systems

## 🚀 Project Overview

The AI Coding Assistant processes a code snippet through a structured pipeline of specialized agents:

1. AnalyzerAgent — performs static analysis
2. OptimizerAgent — improves and rewrites the code
3. DocAgent — generates documentation
4. Supervisor — orchestrates the entire workflow
5. State — maintains shared data across all agents

This design mirrors real AI orchestration systems used in production environments.

## 📦 Requirements

- Python **3.11+**
- pip (recommended)
- Optional: local LLM runtime (Ollama, LM Studio, etc.)

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