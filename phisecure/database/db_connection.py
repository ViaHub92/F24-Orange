from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=None):
    app = Flask(__name__)
    
    # Default to an empty configuration if none is provided
    app.config.from_object(config_class or 'config.Config')
    
    db.init_app(app)
    
    return app
