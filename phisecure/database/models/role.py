""" Import the database connection object (db) from the db_connection module.
"""
from database.db_connection import db

# Define the role model
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", backref="role")

    def __repr__(self) -> str:
        return "<Role %r>" % self.name
