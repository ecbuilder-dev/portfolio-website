from src.data import load_content

def test_load_content_italian_has_expected_keys():
    content = load_content("it")
    assert set(["nome", "ruolo", "tagline", "progetti", "competenze", "esperienze", "email"]) <= set(content.keys())


def test_load_content_english_has_expected_keys():
    content = load_content("en")
    assert content["progetti"][0]["descrizione"] != load_content("it")["progetti"][0]["descrizione"]