""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db


class Instructor(db.Model):
    """
    Represents a instructor user in the database.
    
    Colums:
    id: primary key for instructor
    username: instructor username.
    password_hash: hashed password of instructor
    email: instructor email.
    first_name: instructor name
    last_name: instructor last name:
    course: list of courses taught by the instructor.
    """
    __tablename__ = "instructors"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    
    courses = db.relationship("Course", backref="instructor")
    
 