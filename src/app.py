from flask import Flask, render_template
from flask_babel import Babel
from src.data import PROGETTI, COMPETENZE, ESPERIENZE, EMAIL_CONTATTO

LINGUE_SUPPORTATE = ["it", "en"]

def create_app():
    app = Flask(__name__)
    app.config["LANGUAGES"] = LINGUE_SUPPORTATE
    app.config["BABEL_DEFAULT_LOCALE"] = "it"

    babel = Babel()

    def get_locale():
        return getattr(request, "portfolio_locale", "it")

    babel.init_app(app, locale_selector=get_locale)

    from flask import request

    def render_home():
        return render_template(
            "index.html",
            nome="Alessandro Casamassima",
            ruolo="Full Stack Developer",
            tagline="Java, C#, TypeScript, Angular",
            progetti=PROGETTI,
            competenze=COMPETENZE,
            esperienze=ESPERIENZE,
            email=EMAIL_CONTATTO,
        )

    def _render_localized_home(locale):
        request.portfolio_locale = locale
        return render_home()

    @app.route("/")
    def home():
        return _render_localized_home("it")

    @app.route("/en/")
    def home_en():
        return _render_localized_home("en")

    app.jinja_env.globals["get_locale"] = get_locale

    return app
