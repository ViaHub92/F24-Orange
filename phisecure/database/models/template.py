"""Import the database connection object (db) from the backend.project module."""

import enum
from datetime import datetime, timezone
from backend.project import db
from sqlalchemy import Enum
from sqlalchemy.orm import relationship


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
    difficulty_level = db.Column(Enum(DifficultyLevel), nullable=False)
    sender_template = db.Column(db.String(120), nullable=False)
    subject_template = db.Column(db.String(120), nullable=False)
    body_template = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(100))
    template_redflag=db.Column(db.Text, nullable=True)
    
    phishing_emails = db.relationship("PhishingEmail", back_populates="template", lazy=True)
    tags = db.relationship("Tag", secondary="template_tags", back_populates="templates")
    
    def serialize(self):
        """
         Convert model of a phishing template into a serializable dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'difficulty_level': self.difficulty_level.value,
            'sender_template': self.sender_template,
            'subject_template': self.subject_template,
            'body_template': self.body_template,
            'link': self.link, 
            'template_redflag': self.template_redflag

        }
        
class Tag(db.Model):
    """can represent keyword associated with a user based on questionnaire answers and phishing templates
    Args:
        db (_type_): _description_
    """
    # create id column and name
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    templates = relationship("Template", secondary="template_tags", back_populates="tags")
    
    

class TemplateTag(db.Model):
    """Association table for many-to-many relationship between Template and Tag
    Args:
        db (_type_): _description_
    """
    __tablename__ = "template_tags"
    template_id = db.Column(db.Integer, db.ForeignKey('phishing_templates.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def serialize(self):
        """
        Convert model of a template tag into a serializable dictionary
        """
        return {
            'template_id': self.template_id,
            'tag_id': self.tag_id
        }