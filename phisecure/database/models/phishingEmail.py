""" Import the database connection object (db) from the db_connection module.
"""
from datetime import datetime, timezone
from database.db_connection import db



# Define email
class Phishingemail(db.Model):
    """
    Represents an phishing email in the database.
    
    Columns:
    id: primary key for the phishing email.
    sender: email address of the student who sends the phishing eamil
    recipient: email address of the sudent recipient who gets the phishing email
    sent_at: timestamp when the email was sent.
    subject: subject line of the email
    body: content of the email
   
    
    """
    __tablename__ = "phishing_emails"
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    
    #relationships
    sender = db.relationship("Student", foreign_keys=[sender_id], backref="sent_phishing_emails", lazy=True)
    recipient = db.relationship("Student", foreign_keys=[recipient_id], backref="received_phishing_emails", lazy=True)
    analytics = db.relationship("Analytics", backref="phishing_email", lazy=True)
