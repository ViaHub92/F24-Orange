""" Import the database connection object (db) from the db_connection module.
"""
from database.db_connection import db


# Define the user model
class User(db.Model):
    """
    *deleting the class after tests*
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    inbox_id = db.Column(db.Integer, db.ForeignKey("inbox.id"), nullable=False)

    def __repr__(self) -> str:
        return "<User %r>" % self.username
