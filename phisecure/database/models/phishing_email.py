import uuid
from datetime import datetime, timezone
from backend.project import db


class PhishingEmail(db.Model):
    """
    Represents a phishing email in the database.
    
    Columns:
    id: primary key for the email.
    sender: email address of the sender
    recipient: email address of the recipient.
    sent_at: timestamp when the email was sent.
    subject: subject line of the email
    body: content of the email
    inbox_id: foreign key referencing the inbox associated with the email.
    template_id: foreign key referencing the template used to create the email.
    
    """
    __tablename__ = "phishing_emails"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    red_flag = db.Column(db.Text, nullable=True)
    inbox_id = db.Column(db.Integer, db.ForeignKey("inbox.id"), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("phishing_templates.id"), nullable=False)
    #Attribute of the PhishingEmail model. it is deinfed using the relationship function that creates a realationship with user interaction model
    interactions = db.relationship("UserInteraction", back_populates="phishing_email")
    template = db.relationship("Template", back_populates="phishing_emails")