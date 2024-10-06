""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db


#Define course
class Course(db.Model):
    """
    Represents a course in the database
    
    Columns:
    id: primary key for the course
    course_name: name of the course
    instructor_id: foreign key referencing the instructor who teaches the course
    students: students enrolled in the course.
    """
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructors.id"))
    
    students = db.relationship("Student", backref="course")
    
