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

def test_home_page_shows_projects_section(client):
    response = client.get("/")
    assert b"progetti" in response.data.lower()

def test_home_page_lists_at_least_one_project(client):
    response = client.get("/")
    # verifichiamo la presenza di un contenitore di progetti, non un titolo specifico
    assert response.data.lower().count(b"<article") >= 1

def test_home_page_shows_skills_section(client):
    response = client.get("/")
    assert b"competenze" in response.data.lower()

def test_home_page_shows_experience_section(client):
    response = client.get("/")
    assert b"esperienze" in response.data.lower()

def test_home_page_shows_contact_link(client):
    response = client.get("/")
    assert b"mailto:" in response.data.lower()

def test_static_css_is_referenced(client):
    response = client.get("/")
    assert b'rel="stylesheet"' in response.data

def test_static_css_file_is_served(client):
    response = client.get("/static/style.css")
    assert response.status_code == 200

def test_default_locale_is_italian(client):
    response = client.get("/")
    assert b"lang=\"it\"" in response.data

def test_english_locale_route(client):
    response = client.get("/en/")
    assert response.status_code == 200
    assert b"lang=\"en\"" in response.data

def test_first_project_descriptions_differs_between_languages(client):
    from src.data import get_progetti
    descrizione_it = get_progetti("it")[0]["descrizione"]
    descrizione_en = get_progetti("en")[0]["descrizione"]
    assert descrizione_it != descrizione_en