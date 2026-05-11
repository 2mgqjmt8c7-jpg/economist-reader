import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    entries = data.get("entries", [])
    if not entries:
        return jsonify({"error": "No entries provided"}), 400

    prompt = f"""You are a vocabulary teacher for French students preparing competitive exams (grandes écoles concours, English section).

For each word or expression below, produce exactly one Anki card on a single line in this format:
FR_TRANSLATION|ENTRY — DEFINITION_EN (1 clear sentence, adapted for advanced non-native learners). Ex: EXAMPLE (short original English sentence using the entry naturally).

Rules:
- One line per entry, no header, no extra text, no markdown
- FR_TRANSLATION first (concise French translation, 1-4 words)
- Then the English entry, an em dash, then the definition, then Ex: and the example
- For multi-word expressions, treat the whole expression as one entry
- Definition must be precise and lexically focused
- Example must be original and contextually natural

Entries: {' / '.join(entries)}"""

    resp = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 2000,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=30,
    )

    if resp.status_code != 200:
        return jsonify({"error": resp.text}), 500

    result = resp.json()
    text = "".join(b.get("text", "") for b in result.get("content", []))
    return jsonify({"deck": text.strip()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
