from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Demo endpoint for handling Slack events.
    Production logic and secrets are intentionally omitted.
    """
    data = request.json
    user = data.get("user", "unknown")

    return jsonify({
        "status": "received",
        "user": user,
        "message": "Demo standup event processed"
    })

if __name__ == "__main__":
    app.run(debug=True)
