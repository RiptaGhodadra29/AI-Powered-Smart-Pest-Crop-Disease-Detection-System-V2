from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_prediction():

    response = client.post(
        "/predict/disease",
        json={
            "user_id": 1,
            "image_id": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction_id" in data
    assert "class_name" in data
    assert "confidence" in data
    assert "model_name" in data
    assert "recommendation" in data