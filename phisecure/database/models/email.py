""" Import the database connection object (db) from the db_connection module.
"""
from datetime import datetime, timezone
from database.db_connection import db



# Define email
class Email(db.Model):
    """
    Represents an email in the database.
    
    Columns:
    id: primary key for the email.
    sender: email address of the sender
    recipient: email address of the recipient.
    sent_at: timestamp when the email was sent.
    subject: subject line of the email
    body: content of the email
    inbox_id: foreign key referencing the inbox associated with the email.
    
    
    """
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    inboxs = db.Column(db.Integer, db.ForeignKey("inbox.id"), nullable=False)
    
