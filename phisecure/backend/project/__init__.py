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
    app.config['SECRET_KEY'] = 'your_super_secret_key'
    db.init_app(app)
    
    from project.routes import routes
    from project.blueprints.account import account
    from project.blueprints.messaging import messaging
    app.register_blueprint(routes)
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(messaging, url_prefix='/messaging')

    with app.app_context():
        db.create_all()  # Ensure this creates tables for the models

    return app
