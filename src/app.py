from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template(
            "index.html",
            nome="Alessandro Casamassima",
            ruolo="Full Stack Developer",
            tagline="Java, C#, TypeScript, Angular",
        )

    return app
