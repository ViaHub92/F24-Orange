"""Import the database connection object (db) from the backend.project module."""

import enum
from datetime import datetime, timezone
from backend.project import db
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
    """*Still working on it*

    Represents an email template in the database table.

    Columns:
    id: id for the template.
    name: the name of the template.
    description: description of the template.
    category: categories i.e finance related, credentials, employement scam
    diffuclty_level: level of diffculty of the template
    sent_by: f
    recipient: foreign key of student who gets the phishing template.
    subject: subject line of the template.
    body: content of the template.
    """

    __tablename__ = "phishing_templates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(250))
    tags = db.Column(db.String(120), nullable=False, index=True)
    difficulty_level = db.Column(Enum(DifficultyLevel), nullable=False)
    subject_temlpate = db.Column(db.String(120), nullable=False)
    body_template = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(100))
    
    phishing_emails = db.relationship("PhishingEmail", back_populates="template", lazy=True)
    def serialize(self):
        """
         Convert model of a phishing template into a serializable dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'tags': self.tags,
            'difficulty_level': self.difficulty_level.value,
            'subject_template': self.subject_template,
            'body_template': self.body_template,
            'link': self.link,  

        }