""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db



class UserInteraction(db.Model):
    """
    model for user interaction with phishing templates
    """
    __tablename__ = "user_interaction"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    phishing_email_id = db.Column(db.Integer, db.ForeignKey("phishing_emails.id"), nullable=False)
    opened = db.Column(db.Boolean, default=False)
    link_clicked = db.Column(db.Boolean, default=False)
    replied = db.Column(db.Boolean, default=False)
    reported = db.Column(db.Boolean, default=False)
    #Attribute of the UserInteraction model. it is deinfed using the relationship function that creates a realationship with phishing email model
    phishing_email = db.relationship("PhishingEmail", back_populates="interactions") 
    #Attribute of the UserInteraction model. it is deinfed using the relationship function that creates a realationship with student model
    student = db.relationship("Student", back_populates="interactions")
    
