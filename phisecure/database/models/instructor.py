""" Import the database connection object (db) from the db_connection module.
"""
from backend.project import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


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
    
    @property
    def password(self):
        """ fetches the password of the instructor
        

        Raises:
            AttributeError: Password is not a readable attribute
        """
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        """ sets the password of the instructor and hashes it

        Args:
            password (_type_): password of the instructor
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        """ checks if the password is correct

        Args:
            password (_type_): password of the instructor

        Returns:
            _type_: True if the password is correct, False otherwise
        """
        return bcrypt.check_password_hash(self.password_hash, password)
    