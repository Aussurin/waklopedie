from flask import Flask
from apps.waklopedie import init_waklopedie_routes

__version__ = '0.1.0'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('default_settings.cfg')

    # Initialiser les routes pour Waklopedie
    init_waklopedie_routes(app)

    return app