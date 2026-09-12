from pathlib import Path
import yaml

CONTENT_DIR = Path(__file__).parent.parent / "content"


def load_content(locale):
    path = CONTENT_DIR / f"{locale}.yaml"
    if not path.exists():
        path = CONTENT_DIR / "it.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)