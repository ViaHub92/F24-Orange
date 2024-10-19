""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db

class Student(db.Model):
    """
    Represents a student user in the database.
    
    Columns:
    id: primary key
    username: username of student
    password_hash: hashed password of the student
    email: student email.
    first_name: first name of student
    last_name: last name of student
    inbox_id: foreign key referencing the student's inbox
    course_id: foreign key referencing the student's course.
    """
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    inbox_id = db.Column(db.Integer, db.ForeignKey("inbox.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    
    interactions = db.relationship("UserInteraction", backref="student", lazy=True)
    

    def __repr__(self) -> str:
        return "<User %r>" % self.username