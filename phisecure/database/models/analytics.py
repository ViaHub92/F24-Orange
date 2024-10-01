""" Import the database connection object (db) from the db_connection module.
"""
from datetime import datetime
from database.db_connection import db


class Analytics(db.Model):
    """
    Represents analytics of phishing simulation results
    """
    __tablename__ = "analytics"
    id = db.Column(db.Integer, primary_key=True)
    links_clicked = db.Column(db.Integer, nullable=False, default=0)
    emails_reported = db.Column(db.Integer, nullable=False, default=0)
    emails_opened = db.Column(db.Integer, nullable=False, default=0)
    attachments_downloaded = db.Column(db.Integer, nullable=False, default=0)
    response_time = db.Column(db.DateTime, nullable=True, default=None)
    phishing_email_id = db.Column(db.Integer, db.ForeignKey("phishing_emails.id"), nullable=False)
    
    phishing_email= db.relationship("PhishingEmail", backref="analytics", lazy=True)