""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db

class UserProfile(db.Model):
    """
    Represents the profile personalization for student users for templates
    id: primary key for user profile
    name: name of the student user
    age: age of the student user
    location: location (city,State)
    major: major at university
    courses: list of courses the user is currently enrolled in
    prefered_device: user prefered device to i.e desktop, mobile phone, laptop, tablet
    prefered_social_media: user prefered social media i.e (facebook, twitter, instagram, tiktok)
    use_2fa: Does user use sometype of 2 factor authentication 
    student_id: foreign key referencing the userprofile of the student user.
    
    """
    __tablename__ = "userProfile"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    major = db.Column(db.String(128), nullable=False)
    courses = db.Column(db.Text, nullable=False)
    prefered_device = db.Column(db.String(128))
    prefered_social_media = db.Column(db.String(128))
    use_2fa = db.Column(db.Boolean, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False, unique=True)
    
    student = db.relationship("Student", back_populates="profile")
    