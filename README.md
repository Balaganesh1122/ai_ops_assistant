# 🤖 AI Operations Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Deploment is live at : 
[Streamlit App](https://aiopsassistant-fflhgn4ruugovxpxxpquac.streamlit.app/)

A powerful, **agentic AI agent** that transforms natural language requests into executed actions. Built with a robust **Multi-Agent Architecture**, it autonomously plans, executes, and validates tasks using real-world APIs.

---

## ✨ Key Features
*   **🧠 Multi-Agent Core**: Decoupled *Planner*, *Executor*, and *Verifier* agents for reliable autonomy.
*   **🔌 Real-Time Integrations**: Live connectivity to **GitHub** and **OpenWeatherMap**.
*   **🛡️ Robust Error Handling**: Self-correcting retry logic and graceful failure management.
*   **⚡ Local-First**: Full privacy and speed by running entirely on `localhost`.
*   **💎 Dual Interface**: Interact via a polished **Streamlit UI** or a raw **FastAPI** backend.

---

## 🏗 Architecture

The system implements a **Chain-of-Thought** workflow:

1.  **Planner Agent (`agents/planner.py`)**
    *   *Role*: The Brain.
    *   *Logic*: Analyzes user input --> Selects tools --> Generates a JSON execution plan.
2.  **Executor Agent (`agents/executor.py`)**
    *   *Role*: The Hands.
    *   *Logic*: Iterates through the plan --> Calls specific API tools --> Captures raw data.
3.  **Verifier Agent (`agents/verifier.py`)**
    *   *Role*: The Auditor.
    *   *Logic*: Validates execution results --> Checks for errors -->Synthesizes the final natural language answer.

---

## � Project Structure

```bash
ai_ops_assistant/
├── 🤖 agents/              # The reasoning core
│   ├── planner.py          # Generates execution plans
│   ├── executor.py         # Runs the tools
│   └── verifier.py         # Validates results
├── 🛠️ tools/               # Real-world API integrations
│   ├── github_tool.py      # GitHub Search API
│   └── weather_tool.py     # OpenWeatherMap API
├── 🧠 llm/                 # Model abstractions
│   ├── gemini_client.py    # Google Gemini Interface
│   └── openai_client.py    # OpenAI Interface (Backup)
├── 📱 main.py              # FastAPI Backend Entrypoint
├── 🖥️ ui.py                # Streamlit Frontend
└── ⚙️ .env                 # API Keys and Secrets
```

---

## 🚀 Setup & Installation

### 1. Prerequisites
*   Python 3.8 or higher.
*   API Keys for **GitHub**, **OpenWeatherMap**, and **Google Gemini/OpenAI**.

### 2. Installation
```powershell
# 1. Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (see `.env.example`):
```env
# LLM Provider (Choose One)
GEMINI_API_KEY=AIzaSy...
# OPENAI_API_KEY=sk-...

# Tool Configs
GITHUB_TOKEN=ghp_...
WEATHER_API_KEY=a1b2c3...
```

### 4. Running the App
**Option A: The Beautiful UI (Recommended)**
```powershell
streamlit run ui.py
```
> Access at: `http://localhost:8501`

**Option B: The API Backend**
```powershell
uvicorn main:app --reload
```
> REST Docs at: `http://localhost:8000/docs`

---

## 🧪 Test Drives (Example Prompts)

Try these commands to see the agents in action:

| Complexity | Prompt | What it Tests |
| :--- | :--- | :--- |
| **Simple** | *"Find the top 5 machine learning repositories on GitHub."* | Single-tool usage (GitHub) |
| **Real-time** | *"What is the current weather in Bangalore?"* | Real API connectivity (Weather) |
| **Complex** | *"Check the weather in London and then find a python weather library on GitHub."* | Multi-step planning & context switching |
| **Logic** | *"Hello, who are you?"* | Pure LLM reasoning (No tools) |

---

## ⚠️ Limitations & Tradeoffs
*   **Sequential Execution**: Tools are currently called one-by-one. Future updates will support parallel execution (`asyncio`).
*   **LLM Dependency**: The system relies on the LLM to produce strict JSON. While retry logic handles most errors, extremely malformed responses may cause failures.
*   **Stateless**: The agents treat each request independently and do not maintain long-term memory of previous conversations.

---

## 🔧 Troubleshooting

**Q: "Invalid API Key" (401 Error)?**
*   **Fix**: Verify your keys in `.env`. Note that new OpenWeatherMap keys take **10-15 minutes** to activate.

**Q: "Bad Credentials" (GitHub)?**
*   **Fix**: Ensure your GitHub token starts with `ghp_` and has `repo` access scope.


