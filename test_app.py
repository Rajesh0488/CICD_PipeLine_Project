import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "success"


def test_health_success(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_status_success(client):
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_invalid_route(client):
    response = client.get("/invalid")

    assert response.status_code == 404