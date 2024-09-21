from datetime import datetime, timezone
from project import db





#Define the role model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='role')
    
    def __repr__(self) -> str:
        return '<Role %r>' % self.name
    

#Define the user model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)
    inbox_id = db.Column(db.Integer, db.ForeignKey('userInbox.id'), nullable=False)
    
    def __repr__(self) -> str:
        return '<User %r>' % self.username
    

#Define user inbox
class Inbox(db.Model):
    __tablename__ = 'userInbox'
    id = db.Column(db.Integer, primary_key=True)
    emails = db.relationship('Email', backref='inbox')
    
    
    

#Define email
class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    is_read= db.Column(db.Boolean, default=False)
    inboxs = db.Column(db.Integer, db.ForeignKey('userInbox.id'), nullable=False)
    
    
    
