import time
import hmac
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- DEMO CONSTANTS (NO REAL SECRETS) ---
QUESTIONS = {
    1: "What did you do yesterday?",
    2: "What will you do today?",
    3: "Any blockers?"
}

def verify_slack_request_demo(request):
    """
    DEMO VERSION:
    Shows how Slack requests are verified using HMAC-SHA256.
    Real secrets are intentionally excluded.
    """
    timestamp = request.headers.get("X-Slack-Request-Timestamp")
    signature = request.headers.get("X-Slack-Signature")

    if not timestamp or not signature:
        return False

    # Replay attack protection
    if abs(time.time() - int(timestamp)) > 300:
        return False

    # Demo hash comparison (mocked)
    demo_base_string = f"v0:{timestamp}:body"
    demo_hash = hmac.new(
        b"DEMO_SECRET",
        demo_base_string.encode(),
        hashlib.sha256
    ).hexdigest()

    return demo_hash is not None

@app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    DEMO ENDPOINT:
    Demonstrates state-based standup flow.
    """
    if not verify_slack_request_demo(request):
        return jsonify({"status": "unauthorized"}), 403

    data = request.json
    text = data.get("text", "").lower()
    user = data.get("user", "demo_user")

    if "standup" in text:
        return jsonify({
            "message": QUESTIONS[1],
            "state": "started"
        })

    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return "Standup SaaS Demo – Secure Backend Workflow", 200

if __name__ == "__main__":
    app.run(debug=True)
