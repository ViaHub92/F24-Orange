""" Import the database connection object (db) from the db_connection module.
"""
from datetime import datetime, timezone
from database.db_connection import db




class Template(db.Model):
    """
    *Still working on it*
    
    Represents an email template in the database table.
    
    Columns:
    id: id for the template.
    name: the name of the template.
    description: description of the template.
    subject: subject line of the template.
    body: content of the template.
    """
    __tablename__ = "templates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(120), nullable=False)
    