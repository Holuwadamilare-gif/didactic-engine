# DIDACTIC-ENGINE — app.py
# Port: 14831 (Rare Prime Port)
# Run: pip install flask && python app.py

import os
from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)

PORT = int(os.environ.get("DIDACTIC_ENGINE_PORT", os.environ.get("PORT", 14831)))
HOST = os.environ.get("HOST", "0.0.0.0")

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "engine": "DIDACTIC-ENGINE",
        "status": "alive",
        "port": PORT,
        "throne": "active",
        "dragon": "guarding",
        "secret_type": "[a-z] + numeric prime vault",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/vault/status", methods=["GET"])
def vault_status():
    return jsonify({
        "secret_configured": bool(os.environ.get("DIDACTIC_SECRET")),
        "numeric_key_configured": bool(os.environ.get("DIDACTIC_NUMERIC_KEY")),
        "port": PORT
    })

@app.route("/engine/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    inp = data.get("input")
    if not isinstance(inp, str) or len(inp) > 1000:
        return jsonify({"error": "Invalid input — must be string <= 1000 chars"}), 400
    return jsonify({"echo": inp, "engine": "DIDACTIC-ENGINE"})

if __name__ == "__main__":
    print(f"🐉 DIDACTIC-ENGINE listening on http://{HOST}:{PORT}")
    print(f"   Throne: active | Dragon: guarding | Port: {PORT}")
    app.run(host=HOST, port=PORT, debug=False)
