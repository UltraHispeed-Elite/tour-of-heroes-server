from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, origins=["http://127.0.0.1:4200", "*"])
    
    from .extensions import init_extensions

    init_extensions()

    from heroes_service.blueprints.heroes_bp.heroes_routes import (
        heroes_bp,
    )
    app.register_blueprint(heroes_bp, url_prefix='/api/heroes')

    return app