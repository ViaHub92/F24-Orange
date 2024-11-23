"""Import the database connection object (db) from the backend.project module."""

import enum
from datetime import datetime, timezone
from backend.project import db
from sqlalchemy import Enum
from sqlalchemy.orm import relationship


class DifficultyLevel(enum.Enum):
    """
    Pre defined Enumerator for difficulty levels
    Each template has a diffculty level ranging from beginner, intermediate, and advanced
    """

    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class Template(db.Model):
    """*Still working on it*

    Represents an email template in the database table.

    Columns:
    id: id for the template.
    name: the name of the template.
    description: description of the template.
    category: categories i.e finance related, credentials, employement scam
    diffuclty_level: level of diffculty of the template
    sent_by: f
    recipient: foreign key of student who gets the phishing template.
    subject: subject line of the template.
    body: content of the template.
    """

    __tablename__ = "phishing_templates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(250))
    difficulty_level = db.Column(Enum(DifficultyLevel), nullable=False)
    sender_template = db.Column(db.String(120), nullable=False)
    subject_template = db.Column(db.String(120), nullable=False)
    body_template = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(100))
    template_redflag=db.Column(db.Text, nullable=True)
    
    phishing_emails = db.relationship("PhishingEmail", back_populates="template", lazy=True)
    tags = db.relationship("Tag", secondary="template_tags", back_populates="templates")
    
    def serialize(self):
        """
         Convert model of a phishing template into a serializable dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'difficulty_level': self.difficulty_level.value,
            'sender_template': self.sender_template,
            'subject_template': self.subject_template,
            'body_template': self.body_template,
            'link': self.link, 
            'template_redflag': self.template_redflag

        }
        
class Tag(db.Model):
    """can represent keyword associated with a user based on questionnaire answers and phishing templates
    Args:
        db (_type_): _description_
    """
    # create id column and name
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    templates = relationship("Template", secondary="template_tags", back_populates="tags")
    student_profiles = relationship("StudentProfile", secondary="student_profile_tags", back_populates="tags")

    
class StudentProfile(db.Model):
    """Represents a student profile in the database table.
    Args:
        db (_type_): _description_
    """
    __tablename__ = "student_profiles"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    email_used_for_platforms = db.Column(db.String(120), nullable=False)
    employement_status = db.Column(db.String(120), nullable=False)
    employer = db.Column(db.String(120), nullable=True)
    risk_level = db.Column(db.String(120), nullable=False)
    attention_to_detail = db.Column(db.String(120), nullable=False)
    tags = relationship("Tag", secondary="student_profile_tags", back_populates="student_profiles")
    responses = relationship("Response", back_populates="student_profile")
    
    def serialize(self):
        """
        Convert model of a student profile into a serializable dictionary
        """
        return {
            'id': self.id,
            'student_id': self.student_id,
            'first_name': self.first_name,
            'email_used_for_platforms': self.email_used_for_platforms,
            'employement_status': self.employement_status,
            'employer': self.employer,
            'risk_level': self.risk_level,
            'attention_to_detail': self.attention_to_detail,
            'tags': [tag.serialize() for tag in self.tags],
            'responses': [response.serialize() for response in self.responses]
        }
    
    def get_answers_from_questionnaire(self, questionnaire_id):
        """
        Get the answers from a questionnaire
        Args:
            questionnaire_id (_type_): _description_
        """
        answers = []
        for response in self.responses:
            if response.questionnaire_id == questionnaire_id:
                for answer in response.answers:
                    answers.append({
                        'question_id': answer.question_id,
                        'answer_text': answer.answer_text
                    })
        return answers
    
    def update_attributes_from_answers(self, questionnaire_id):
        """ Update information in student profile such as employement status and employer from questionnaire

        Args:
            questionnaire_id (_type_): _description_

        """
        answers = self.get_answers_from_questionnaire(questionnaire_id)
        for answer in answers:
            question_id = answer['question_id']
            answer_text = answer['answer_text']
            
            if question_id == 29:
                if answer_text.lower() == 'n/a':
                    self.employement_status = 'Unemployed'
                    self.employer = None
                else:
                    self.employement_status = 'Employed'
                    self.employer = answer_text
            
        db.session.commit()
        
        
    def assign_tags_to_profiles(self, questionnaire_id):
        """Assign tags to student profiles based on questionnaire answers

        Args:
            question_id (_type_):   question id of the questionnaire answer to be used to assign tags

        """
        answers = self.get_answers_from_questionnaire(questionnaire_id)
        for answer in answers:
            question_id = answer['question_id']
            answer_text = answer['answer_text']
            #question 1: Phishing awareness
            if question_id == 1:
                if answer_text.lower() == 'yes':
                    tag = Tag.query.filter_by(name='phishing-aware').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='phishing-unaware').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                        
                #question 2: Password change frequency
            elif question_id == 2:
                if answer_text.lower() == 'every month':
                    tag = Tag.query.filter_by(name='highly-security-conscious').first()
                elif answer_text.lower() == 'every 3 months':
                    tag = Tag.query.filter_by(name='security-conscious').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'every 6 months':
                    tag = Tag.query.filter_by(name='moderate-security-conscious').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'every year':
                    tag = Tag.query.filter_by(name='low-security-awareness').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'never':
                    tag = Tag.query.filter_by(name='high-risk').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 3: Do you reuse passwords for multiple accounts?
            elif question_id == 3:
                if answer_text.lower() == 'yes':
                    tag = Tag.query.filter_by(name='password-reuse').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='unique-password-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 4: Do you check the senders email address before clicking on a link or replying to emails?
            elif question_id == 4:
                if answer_text.lower() == 'yes':
                    tag = Tag.query.filter_by(name='vigilant-email-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='link-clicker').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 5: Do you shop online? if yes, which platform do you use?
            elif question_id == 5:
                if answer_text.lower() == 'amazon':
                    tag = Tag.query.filter_by(name='amazon-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'ebay':
                    tag = Tag.query.filter_by(name='ebay-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'walmart':
                    tag = Tag.query.filter_by(name='walmart-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'Target':
                    tag = Tag.query.filter_by(name='target-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'Other retail websites':
                    tag = Tag.query.filter_by(name='other-online-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='non-online-shopper').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 6: Do you manage your finances online? if yes, which platform do you use?
            elif question_id == 6:
                if answer_text.lower() == 'banking apps':
                    tag = Tag.query.filter_by(name='banking-app-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'paypal':
                    tag = Tag.query.filter_by(name='paypal-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'venmo':
                    tag = Tag.query.filter_by(name='venmo-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'cash app':
                    tag = Tag.query.filter_by(name='cash-app-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'investment platforms':
                    tag = Tag.query.filter_by(name='investment-app-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='non-online-banking-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 7: Which work or school-related tools do you use frequently?
            elif question_id == 7:
                if answer_text.lower() == 'microsoft-office-365':
                    tag = Tag.query.filter_by(name='microsoft-tools-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'google-workspace':
                    tag = Tag.query.filter_by(name='google-tools-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'Zoom':
                    tag = Tag.query.filter_by(name='zoom-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'Slack':
                    tag = Tag.query.filter_by(name='slack-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'Microsoft-Teams':
                    tag = Tag.query.filter_by(name='microsoft-teams-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='other-work-school-tools-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 8: What type of email are you most likely to open immediately?
            elif question_id == 8:
                if answer_text.lower() == 'work/school-related':
                    tag = Tag.query.filter_by(name='work-school-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'personal correspondence':
                    tag = Tag.query.filter_by(name='personal-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'shopping/retail':
                    tag = Tag.query.filter_by(name='shopping-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'financial notifications':
                    tag = Tag.query.filter_by(name='financial-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'social media notifications':
                    tag = Tag.query.filter_by(name='social-media-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='generic-email-priority').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
            
            #question 9: Which social media services do you use?
            elif question_id == 9:
                if answer_text.lower() == 'facebook':
                    tag = Tag.query.filter_by(name='facebook-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'instagram':
                    tag = Tag.query.filter_by(name='instagram-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'twitter':
                    tag = Tag.query.filter_by(name='twitter-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'linkedin':
                    tag = Tag.query.filter_by(name='linkedin-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'snapchat':
                    tag = Tag.query.filter_by(name='snapchat-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                elif answer_text.lower() == 'tiktok':
                    tag = Tag.query.filter_by(name='tiktok-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
                else:
                    tag = Tag.query.filter_by(name='non-social-media-user').first()
                    if tag not in self.tags:
                        self.tags.append(tag)
        db.session.commit()
    
    def get_assigned_tags_from_student_profile(self):
        """ Get the tags assigned to a student profile

        Returns:
            _type_: list of tags assigned to the student profile
        """
        
        return [tag.name for tag in self.tags]
            
           
class TemplateTag(db.Model):
    """Association table for many-to-many relationship between Template and Tag
    Args:
        db (_type_): _description_
    """
    __tablename__ = "template_tags"
    template_id = db.Column(db.Integer, db.ForeignKey('phishing_templates.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def serialize(self):
        """
        Convert model of a template tag into a serializable dictionary
        """
        return {
            'template_id': self.template_id,
            'tag_id': self.tag_id
        }

class StudentProfileTag(db.Model):
    """Association table for many-to-many relationship between StudentProfile and Tag
    Args:
        db (_type_): _description_
    """
    __tablename__ = "student_profile_tags"
    student_profile_id = db.Column(db.Integer, db.ForeignKey('student_profiles.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def serialize(self):
        """
        Convert model of a student profile tag into a serializable dictionary
        """
        return {
            'student_profile_id': self.student_profile_id,
            'tag_id': self.tag_id
        }
