from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_history():

    response = client.get(
        "/history/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "history" in data
    assert isinstance(
        data["history"],
        list
    )