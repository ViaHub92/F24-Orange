""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db



class Inbox(db.Model):
    """
    Represents an Inbox for students in virtual phishing environment.
    
    Columns:
    id: Primary key for the inbox
    emails: list of emails associated with the inbox
    """
    __tablename__ = "inbox"
    id = db.Column(db.Integer, primary_key=True)
    emails = db.relationship("Email", backref="inbox")
    phishing_emails = db.relationship("PhishingEmail", backref="inbox")
