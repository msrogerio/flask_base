from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def factory():
    
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    from .main import _main
    app.register_blueprint(_main)

    return app