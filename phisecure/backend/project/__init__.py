# backend/project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from project.routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()  # Ensure this creates tables for the models

    return app
