"""
app.py — Flask web interface for my-first-agent
------------------------------------------------
Run:   python app.py
Open:  http://localhost:5000

NOTE: conversation_history is a single module-level list shared across
all requests. This is intentional for a single-user local app. Do NOT
run this with multiple workers (e.g. gunicorn -w 4) — each worker
would get its own disconnected copy of the history.
"""

from flask import Flask, render_template, request, jsonify
import agent  # imports conversation_history, run_agent_web, etc.

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the chat UI."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Accept a user message, run the agent, return structured JSON.

    Request body:  {"message": "..."}
    Response body: {
        "response":        str,
        "steps":           [...],
        "history_length":  int,
        "error":           str | null
    }
    """
    data = request.get_json(force=True)
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Message cannot be empty."}), 400

    result = agent.run_agent_web(message)
    return jsonify(result)


@app.route("/reset", methods=["POST"])
def reset():
    """
    Clear the conversation history so the agent starts fresh.
    Uses .clear() (not reassignment) to modify the list in-place,
    keeping the reference inside agent.py valid.
    """
    agent.conversation_history.clear()
    return jsonify({"ok": True, "message": "Conversation history cleared."})


if __name__ == "__main__":
    print("Starting ac AI Agent web UI...")
    print("Open your browser at: http://localhost:5000")
    app.run(debug=True, port=5000)
