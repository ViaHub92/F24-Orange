""" Import the database connection object (db) from the db_connection module.
"""
from database.db_connection import db

class Admin(db.Model):
    """
    Represents an administrator user in the database.
    
    Columns:
    id: primary key for the admin
    username: admins username
    password_hash: the hashed password of the amin
    email: admins email
    first_name: admin first name
    last_name: admin last name
    """
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))