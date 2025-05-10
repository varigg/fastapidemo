import os

import pytest
from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app

# Set the TESTING environment variable
os.environ["TESTING"] = "1"


# Create the database schema before running tests
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_create_todo(client):
    response = client.post("/todos/", json={"title": "Test Todo", "description": "This is a test todo."})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"


def test_read_todo(client):
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert "title" in response.json()
    assert response.json()["title"] == "Test Todo"
