from fastapi.testclient import TestClient
from pentest_assistant.backend.api import app


def test_summarize_endpoint():
    client = TestClient(app)
    resp = client.post("/summarize", json={"text": "This is a long note."})
    assert resp.status_code == 200
    data = resp.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
