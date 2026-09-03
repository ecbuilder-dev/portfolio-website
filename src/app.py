from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "<h1>Nome Cognome</h1>"

    return app
