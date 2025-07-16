from flask import Flask, jsonify, Response, request
import os
import json
import time
import logging

from mock_adapter import MockAdapter               # GCP Adapter
from fusion.fusion_engine import FusionEngine      # NCP + GCP Fusion Engine

# Logging setup
logging.basicConfig(level=logging.INFO)

# Flask app init
app = Flask(__name__)

# Consent check for NCP system
CONSENT_GRANTED = os.getenv("XR_NCP_CONSENT", "false").lower() == "true"

# GCP Adapter and NCP Engine
adapter = MockAdapter()
fusion = FusionEngine()

# -----------------------------
# 🔁 ROUTE: GCP + NCP Streaming
# -----------------------------
@app.route("/api/fused_stream")
def fused_stream():
    if not CONSENT_GRANTED:
        def error_stream():
            yield f"data: {json.dumps({'error': 'Consent not granted'})}\n\n"
        return Response(error_stream(), mimetype='text/event-stream')

    def event_stream():
        for _ in range(5):
            gcp_context = adapter.get_context()
            fused = fusion.fuse(gcp_context)
            yield f"data: {json.dumps(fused)}\n\n"
            time.sleep(2)

    return Response(event_stream(), mimetype='text/event-stream')


# --------------------------
# 🔁 ROUTE: NCP Inference API
# --------------------------
@app.route("/api/ncp_context", methods=["POST"])
def ncp_context():
    if not CONSENT_GRANTED:
        return jsonify({
            "error": "User consent not granted. Set XR_NCP_CONSENT=true to enable."
        }), 403

    gcp_data = request.get_json()
    full_context = fusion.fuse(gcp_data)
    logging.info(f"Fused Context Served: {json.dumps(full_context)}")
    return jsonify(full_context)


# --------------------------
# 🔁 ROUTE: NCP Stream via POST
# --------------------------
@app.route("/api/ncp_stream", methods=["POST"])
def ncp_stream():
    if not CONSENT_GRANTED:
        def error_stream():
            yield f"data: {json.dumps({'error': 'Consent not granted'})}\n\n"
        return Response(error_stream(), mimetype='text/event-stream')

    input_data = request.get_json()

    def event_stream():
        for _ in range(5):
            fused = fusion.fuse(input_data)
            yield f"data: {json.dumps(fused)}\n\n"
            time.sleep(2)

    return Response(event_stream(), mimetype='text/event-stream')


# --------------------------
# 🔁 DEBUG ROUTE (GET FUSED)
# --------------------------
@app.route("/api/debug_fused")
def debug_fused():
    dummy_context = adapter.get_context()
    fused = fusion.fuse(dummy_context)
    return jsonify(fused)


# --------------------------
# 🚀 RUN APP
# --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
