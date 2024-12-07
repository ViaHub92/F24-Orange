import uuid
from datetime import datetime, timezone
from backend.project import db
from database.models.user_interaction import UserInteraction
from sqlalchemy import func, cast, Integer


class PhishingEmail(db.Model):
    """
    Represents a phishing email in the database.
    
    Columns:
    id: primary key for the email.
    sender: email address of the sender
    recipient: email address of the recipient.
    sent_at: timestamp when the email was sent.
    subject: subject line of the email
    body: content of the email
    inbox_id: foreign key referencing the inbox associated with the email.
    template_id: foreign key referencing the template used to create the email.
    
    """
    __tablename__ = "phishing_emails"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    red_flag = db.Column(db.Text, nullable=True)
    instructor_feedback = db.Column(db.Text, nullable=True)
    inbox_id = db.Column(db.Integer, db.ForeignKey("inbox.id"), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("phishing_templates.id"), nullable=True)
    peer_phishing_template_id = db.Column(db.Integer, db.ForeignKey("peer_phishing_templates.id"), nullable=True)
    
    #Attribute of the PhishingEmail model. it is deinfed using the relationship function that creates a realationship with user interaction model
    interactions = db.relationship("UserInteraction", back_populates="phishing_email")
    template = db.relationship("Template", back_populates="phishing_emails")
    peer_phishing_template = db.relationship("PeerPhishingTemplate", back_populates="phishing_emails")
    
    @classmethod
    def calculate_interactions_per_email(cls):
        """
        Calculate the number of interactions for each phishing email.
        """
        interactions_per_email = db.session.query(
            cls.id,
            cls.template_id,
            func.sum(UserInteraction.opened(db.Integer)).label("total_opened"),
            func.sum(UserInteraction.link_clicked(db.Integer)).label("total_links_clicked"),
            func.sum(UserInteraction.replied(db.Integer)).label("total_replied")
        ).outerjoin(UserInteraction, cls.id == UserInteraction.phishing_email_id).group_by(cls.id).all()
        
        return interactions_per_email