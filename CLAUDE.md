# CLAUDE.md — Project Context for Claude Code

## Project
**ac AI Agent** — A Python AI agent built with the Anthropic SDK, featuring a CLI and a Flask web UI.

## Key Files
| File | Purpose |
|---|---|
| `agent.py` | Core agent — tools, agentic loop, conversation history |
| `app.py` | Flask web server — `/chat`, `/reset`, `/` routes |
| `templates/index.html` | Chat UI — vanilla HTML/CSS/JS, no frameworks |
| `.env` | API keys (never commit) |
| `files/` | Folder the agent can read/write (never commit) |
| `requirements.txt` | Python dependencies |
| `vercel.json` | Vercel deployment config |

## Environment
- **Python**: 3.14
- **Virtual environment**: `venv/` in project root
- **Activate (Windows/bash)**: `source venv/Scripts/activate`
- **API keys**: stored in `.env` — `ANTHROPIC_API_KEY` and `TAVILY_API_KEY`

## How to Run
```bash
# CLI agent
source venv/Scripts/activate
python agent.py

# Web UI
source venv/Scripts/activate
python app.py
# then open http://localhost:5000
```

## Model
`claude-sonnet-4-5` (set as `MODEL` constant in `agent.py`)

## Tools the Agent Has
| Tool | Function | External API? |
|---|---|---|
| `web_search` | Live web search | Tavily (needs `TAVILY_API_KEY`) |
| `get_weather` | Current weather for any city | Open-Meteo (free, no key) |
| `read_file` | Read files from `files/` folder | No |
| `write_file` | Write files to `files/` folder | No |
| `calculator` | Safe math expression evaluator | No |

## Architecture Notes
- `conversation_history` is a **module-level list** in `agent.py` — shared across all turns in a session
- `run_agent(goal)` → CLI loop, prints to stdout, returns `None`
- `run_agent_web(goal)` → web loop, returns structured `dict` for Flask to serialize as JSON
- All tool errors return structured JSON via `_err(type, message, suggestion)` helper
- `FILES_DIR` = `<project_root>/files/` — all file tool reads/writes are sandboxed here

## Vercel Deployment Notes
- Serverless: `conversation_history` resets between requests (no memory in production)
- Read-only filesystem: `read_file` / `write_file` tools won't work on Vercel
- Set `ANTHROPIC_API_KEY` and `TAVILY_API_KEY` in Vercel environment variables dashboard

## Common Commands
```bash
pip install -r requirements.txt   # install all dependencies
pip freeze > requirements.txt     # update dependencies list
python -c "import agent; import app; print('OK')"  # verify imports
```
