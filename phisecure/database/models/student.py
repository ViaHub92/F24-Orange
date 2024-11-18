""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

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
    
    
    interactions = db.relationship("UserInteraction", back_populates="student")
    #attribute of the Student model. it is deinfed using the relationship function that creates a realationship with Response model
    responses = db.relationship("Response", back_populates="student")
    
    @property
    def password(self):
        """ fetches the password of the student
        

        Raises:
            AttributeError: Password is not a readable attribute
        """
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        """ sets the password of the student and hashes it

        Args:
            password (_type_): password of the student
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        """ checks if the password is correct

        Args:
            password (_type_): password of the student

        Returns:
            _type_: True if the password is correct, False otherwise
        """
        return bcrypt.check_password_hash(self.password_hash, password)
    
   