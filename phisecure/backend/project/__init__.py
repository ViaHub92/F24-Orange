# backend/project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.config import Config

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
   
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'your_super_secret_key'
    db.init_app(app)
    migrate.init_app(app, db)
    
    from backend.project.routes import routes
    from backend.project.blueprints.account import account
    from backend.project.blueprints.messaging import messaging
    from backend.project.blueprints.performance import performance
    from backend.project.blueprints.phishing_templates import phishing_templates
    from backend.project.blueprints.questionnaire import questionnaire
    app.register_blueprint(routes)
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(messaging, url_prefix='/messaging')
    app.register_blueprint(performance, url_prefix='/performance')
    app.register_blueprint(phishing_templates, url_prefix='/phishing')
    app.register_blueprint(questionnaire, url_prefix='/questionnaire')
    
    """
    with app.app_context():
        db.create_all()  # Ensure this creates tables for the models
    """
    return app
