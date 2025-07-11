from flask import Flask, jsonify, Response
import os
import json
import time
import logging
logging.basicConfig(level=logging.INFO)
# Import your adapters
from mock_adapter import MockAdapter

app = Flask(__name__)
CONSENT_GRANTED = os.getenv("XR_GCP_CONSENT", "false").lower() == "true"

# Choose the adapter (in future, could auto-detect platform)
adapter = MockAdapter()

@app.route("/api/context")
def get_context():
    if not CONSENT_GRANTED:
        return jsonify({
            "error": "User consent not granted. Set XR_GCP_CONSENT=true to enable."
        }), 403

    context = adapter.get_context()
    logging.info(f"Context served: {json.dumps(context)}")
    return jsonify(context)

@app.route("/api/stream")
def stream_context():
    if not CONSENT_GRANTED:
        def error_stream():
            yield f"data: {json.dumps({'error': 'Consent not granted'})}\n\n"
        return Response(error_stream(), mimetype='text/event-stream')

    def event_stream():
        for _ in range(5):
            context = adapter.get_context()
            data = json.dumps(context)
            yield f"data: {data}\n\n"
            time.sleep(2)

    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
