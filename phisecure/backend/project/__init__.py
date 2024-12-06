# backend/project/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from backend.config import Config

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
   
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'your_super_secret_key'
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'account.login'
    
    from backend.project.routes import routes
    from backend.project.blueprints.account import account
    from backend.project.blueprints.messaging import messaging
    from backend.project.blueprints.performance import performance
    from backend.project.blueprints.phishing_templates import phishing_templates
    from backend.project.blueprints.questionnaire import questionnaire
    from backend.project.blueprints.course import course
    from backend.project.blueprints.instructor_dashboard import instructor_dashboard
    from backend.project.blueprints.admin_dashboard import admin_dashboard
    from backend.project.blueprints.peer_phishing import peer_phishing
    app.register_blueprint(routes)
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(messaging, url_prefix='/messaging')
    app.register_blueprint(performance, url_prefix='/performance')
    app.register_blueprint(phishing_templates, url_prefix='/phishing')
    app.register_blueprint(questionnaire, url_prefix='/questionnaire')
    app.register_blueprint(course, url_prefix='/course')
    app.register_blueprint(instructor_dashboard, url_prefix='/instructor_dashboard')
    app.register_blueprint(admin_dashboard, url_prefix='/admin_dashboard')
    app.register_blueprint(peer_phishing, url_prefix='/peer_phishing')
    
    """
    with app.app_context():
        db.create_all()  # Ensure this creates tables for the models
    """
    
    return app
