from fastapi.testclient import TestClient
from uuid import uuid4

from backend.main import app

client = TestClient(app)


def test_register_user():
    unique = uuid4().hex[:8]
    username = f"testuser_{unique}"
    email = f"test{unique}@example.com"

    response = client.post(
        "/auth/register",
        json={
            "username": username,
            "email": email,
            "password": "test123"
        }
    )

    assert response.status_code in [200, 201]