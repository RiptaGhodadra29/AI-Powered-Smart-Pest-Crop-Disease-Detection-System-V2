from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_dashboard():

    response = client.get(
        "/dashboard/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "user_id" in data
    assert "total_predictions" in data
    assert "most_detected_disease" in data
    assert "average_confidence" in data