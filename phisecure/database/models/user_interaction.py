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
    template_id = db.Column(db.Integer, db.ForeignKey("phishing_templates.id"), nullable=False)
    opened = db.Column(db.Boolean, default=False)
    link_clicked = db.Column(db.Boolean, default=False)
    replied = db.Column(db.Boolean, default=False)
    reported = db.Column(db.Boolean, default=False)
    

    
