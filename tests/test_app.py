import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_home_page_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_page_renders_template(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()
