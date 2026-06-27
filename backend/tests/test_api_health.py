from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "AI Crop Disease Detection API is running 🚀"
    }