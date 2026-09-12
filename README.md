# Portfolio Website

Sito personale che funge da curriculum online, costruito con Flask seguendo la metodologia TDD.

## Stack
- Python 3
- Flask
- pytest
- Jinja2

## Setup locale
```bash
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Testing
```bash
pytest
```

## Modificare i contenuti
I testi del sito (nome, ruolo, progetti, competenze, esperienze, email) si trovano in:
- `content/it.yaml` (versione italiana)
- `content/en.yaml` (versione inglese)

Modifica questi file, poi fai commit e push: Render effettuerà il deploy automaticamente.