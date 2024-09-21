# backend/project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    
    from project.routes import routes, account
    app.register_blueprint(routes)
    app.register_blueprint(account, url_prefix='/account')
    
    with app.app_context():
        db.create_all()  # Ensure this creates tables for the models

    return app
