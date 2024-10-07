""" Import the database connection object (db) from the db_connection module.
"""
'''
from datetime import datetime, timezone
from backend.project import db
import enum
from sqlalchemy import Enum

class DifficultyLevel(enum.Enum):
    """
    Pre defined Enumerator for difficulty levels
    Each template has a diffculty level ranging from beginner, intermediate, and advanced
    """
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"





class Template(db.Model):
    """
    *Still working on it*
    
    Represents an email template in the database table.
    
    Columns:
    id: id for the template.
    name: the name of the template.
    description: description of the template.
    category: categories i.e finance related, credentials, employement scam
    diffuclty_level: level of diffculty of the template
    sent_by: foreign key of student who sent the template.
    recipient: foreign key of student who gets the phishing template.
    subject: subject line of the template.
    body: content of the template.
    """
    __tablename__ = "phishing_templates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(250), nullable=False)
    diffculty_level = db.Column(Enum(DifficultyLevel), nullable=False)
    sent_by =db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    recipient = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    