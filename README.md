# ac AI Agent

A conversational AI agent built with the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python). Runs as a CLI tool or a Flask web chat UI. The agent remembers your conversation and can search the web, check the weather, do math, and read/write local files.

## Features

| Tool | What it does |
|---|---|
| 🔍 **Web Search** | Live search via [Tavily](https://tavily.com) |
| 🌤️ **Weather** | Real-time weather for any city ([Open-Meteo](https://open-meteo.com), no key needed) |
| 📂 **Read File** | Read text files from the local `files/` folder |
| 💾 **Write File** | Save notes or summaries to the `files/` folder |
| 🧮 **Calculator** | Safely evaluate math expressions |

- **Conversation memory** — the agent remembers everything discussed in a session
- **Structured error handling** — every tool returns actionable error messages so the agent never crashes or hallucinates
- **Web UI** — clean chat interface with inline tool-call blocks and Markdown rendering

## Screenshots

| CLI | Web UI |
|---|---|
| `python agent.py` in terminal | `http://localhost:5000` in browser |

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/arunsakcharoon/my-first-agent.git
cd my-first-agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate   # Windows / Git Bash
# source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API keys
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
```

- Get an Anthropic key at [console.anthropic.com](https://console.anthropic.com)
- Get a free Tavily key at [app.tavily.com](https://app.tavily.com) (1,000 searches/month free)

### 5. Run

**CLI:**
```bash
python agent.py
```

**Web UI:**
```bash
python app.py
# Open http://localhost:5000
```

## Project Structure

```
ac-ai-agent/
├── agent.py            # Core agent — tools, agentic loop, conversation history
├── app.py              # Flask web server
├── templates/
│   └── index.html      # Chat UI (HTML + CSS + vanilla JS)
├── files/              # Folder the agent can read/write (gitignored)
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config
├── .env                # API keys (gitignored — never commit)
└── .gitignore
```

## How It Works

The agent uses the standard **agentic loop**:

```
User message
    → Send to Claude with available tools
    → Claude decides to use a tool
    → Execute the tool locally
    → Send result back to Claude
    → Repeat until Claude returns a final answer
```

Each turn appends to a shared `conversation_history` list, giving Claude full context of everything discussed.

## Deploying to Vercel

1. Push to GitHub
2. Import repo at [vercel.com/new](https://vercel.com/new)
3. Add environment variables in Vercel dashboard:
   - `ANTHROPIC_API_KEY`
   - `TAVILY_API_KEY`
4. Deploy

> **Note:** Vercel is serverless — conversation memory and file tools won't work in production. Web search, weather, and calculator work fine.

## Built With

- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Flask](https://flask.palletsprojects.com)
- [Tavily Search API](https://tavily.com)
- [Open-Meteo Weather API](https://open-meteo.com)
