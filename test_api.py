import json
from app import app

def test_get_context_success():
    # Override consent to True for test
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/api/context")
        assert response.status_code == 200

        data = response.get_json()
        assert "spatial" in data
        assert "social" in data
        assert "environmental" in data
        assert "user" in data

        # Example structure check
        assert "room" in data["spatial"]
        assert "people_nearby" in data["social"]

def test_stream_context_format():
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/api/stream")
        assert response.status_code == 200
        assert response.mimetype == "text/event-stream"

        data_chunks = list(response.response)
        assert len(data_chunks) > 0

        for chunk in data_chunks:
            text = chunk.decode()
            assert text.startswith("data: ")
