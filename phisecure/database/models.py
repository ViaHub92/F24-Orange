from db_connection import db

#Define the role model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Intger, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    

