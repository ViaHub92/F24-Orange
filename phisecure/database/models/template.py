"""Import the database connection object (db) from the backend.project module."""

import enum
from datetime import datetime, timezone
from sqlalchemy import cast, Integer
from backend.project import db
from sqlalchemy.sql import func
from database.models.phishing_email import PhishingEmail
from database.models.user_interaction import UserInteraction
from database.models.student import Student
from database.models.course import Course
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
    body_template = db.Column(db.Text, nullable=False)
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
            'template_redflag': self.template_redflag,
            
            

        }
    
    
        
    @classmethod
    def calculate_interaction_rate(cls, course_id):
        """
        Calculate open rate, click rate, and reply rate for each phishing template in a specific course.
        
        Args:
            course_id (int): The ID of the course.
        
        Returns:
            list: A list of dictionaries containing interaction rates for each template.
        """
        # Get all students in the course
        students = Student.query.filter_by(course_id=course_id).all()
        student_emails = [student.email for student in students]
      

        # Get all phishing emails sent to these students
        phishing_emails = PhishingEmail.query.filter(PhishingEmail.recipient.in_(student_emails)).all()

        
        # Aggregate interactions by template
        interactions_by_template = {}
        for email in phishing_emails:
            if email.template_id not in interactions_by_template:
                interactions_by_template[email.template_id] = {
                    'total_opened': 0,
                    'total_links_clicked': 0,
                    'total_replied': 0,
                    'total_phishing_emails': 0,
                }

            interactions = UserInteraction.query.filter_by(phishing_email_id=email.id).all()
           
            for interaction in interactions:
                interactions_by_template[email.template_id]['total_opened'] += interaction.opened
                interactions_by_template[email.template_id]['total_links_clicked'] += interaction.link_clicked
                interactions_by_template[email.template_id]['total_replied'] += interaction.replied
                interactions_by_template[email.template_id]['total_phishing_emails'] += 1

        # Calculate interaction rates for each template
        rates = []
        for template_id, data in interactions_by_template.items():
            template = cls.query.get(template_id)
            if template is None:
                continue
            
            total_opened = data['total_opened']
            total_links_clicked = data['total_links_clicked']
            total_replied = data['total_replied']
            total_phishing_emails = data['total_phishing_emails']

            open_rate = round((total_opened / total_phishing_emails) * 100, 2) if total_phishing_emails > 0 else 0
            click_rate = round((total_links_clicked / total_phishing_emails) * 100, 2) if total_phishing_emails > 0 else 0
            reply_rate = round((total_replied / total_phishing_emails) * 100, 2) if total_phishing_emails > 0 else 0
           

            rate = {
                'template_id': template_id,
                'template_name': template.name,
                'total_opened': total_opened,
                'total_links_clicked': total_links_clicked,
                'total_replied': total_replied,
                'total_phishing_emails': total_phishing_emails,
                'open_rate': open_rate,
                'click_rate': click_rate,
                'reply_rate': reply_rate,
       
            }

            rates.append(rate)
            
       
        return rates
        

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
    peer_phishing_templates = relationship("PeerPhishingTemplate", secondary="peer_phishing_template_tags", back_populates="tags")
    

    
class StudentProfile(db.Model):
    """Represents a student profile in the database table.
    Args:
        db (_type_): _description_
    """
    __tablename__ = "student_profiles"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    major = db.Column(db.String(120), nullable=False)
    email_used_for_platforms = db.Column(db.String(120), nullable=False)
    employement_status = db.Column(db.String(120), nullable=False)
    employer = db.Column(db.String(120), nullable=True)
    risk_level = db.Column(db.String(120), nullable=False)
    attention_to_detail = db.Column(db.String(120), nullable=False)
    tags = relationship("Tag", secondary="student_profile_tags", back_populates="student_profiles")
    responses = relationship("Response", back_populates="student_profile")
    target_list = db.relationship("TargetList", back_populates="student_profile")
    
    def serialize(self):
        """
        Convert model of a student profile into a serializable dictionary
        """
        return {
            'id': self.id,
            'student_id': self.student_id,
            'first_name': self.first_name,
            'major': self.major,
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
            
            elif question_id == 30:
                self.major = answer_text
            
        db.session.commit()
        
        
    def assign_tags_to_profiles(self, questionnaire_id):
        """Assign tags to student profiles based on questionnaire answers

        Args:
        question_id (_type_):   question id of the questionnaire answer to be used to assign tags

        """
        answers = self.get_answers_from_questionnaire(questionnaire_id)
        tags_to_add = []
        
        for answer in answers:
            question_id = answer['question_id']
            answer_text = answer['answer_text']
            tag_name = None

            # question 1: Phishing awareness
            if question_id == 20:
                if answer_text.lower() == 'yes':
                    tag_name = 'phishing-aware'
                else:
                    tag_name = 'phishing-unaware'

            # question 2: Password change frequency
            elif question_id == 21:
                if answer_text.lower() == 'every month':
                    tag_name = 'highly-security-conscious'
                elif answer_text.lower() == 'every 3 months':
                    tag_name = 'security-conscious'
                elif answer_text.lower() == 'every 6 months':
                    tag_name = 'moderate-security-conscious'
                elif answer_text.lower() == 'every year':
                    tag_name = 'low-security-awareness'
                elif answer_text.lower() == 'never':
                    tag_name = 'high-risk'

            # question 3: Do you reuse passwords for multiple accounts?
            elif question_id == 22:
                if answer_text.lower() == 'yes':
                    tag_name = 'password-reuse'
                else:
                    tag_name = 'unique-password-user'

            # question 4: Do you check the senders email address before clicking on a link or replying to emails?
            elif question_id == 23:
                if answer_text.lower() == 'yes':
                    tag_name = 'vigilant-email-user'
                else:
                    tag_name = 'link-clicker'

            # question 5: Do you shop online? if yes, which platform do you use?
            elif question_id == 24:
                if answer_text.lower() == 'amazon':
                    tag_name = 'amazon-shopper'
                elif answer_text.lower() == 'ebay':
                    tag_name = 'ebay-shopper'
                elif answer_text.lower() == 'walmart':
                    tag_name = 'walmart-shopper'
                elif answer_text.lower() == 'target':
                    tag_name = 'target-shopper'
                elif answer_text.lower() == 'other retail websites':
                    tag_name = 'other-online-shopper'
                else:
                    tag_name = 'non-online-shopper'

            # question 6: Do you manage your finances online? if yes, which platform do you use?
            elif question_id == 25:
                if answer_text.lower() == 'banking apps':
                    tag_name = 'banking-app-user'
                elif answer_text.lower() == 'paypal':
                    tag_name = 'paypal-user'
                elif answer_text.lower() == 'venmo':
                    tag_name = 'venmo-user'
                elif answer_text.lower() == 'cash app':
                    tag_name = 'cash-app-user'
                elif answer_text.lower() == 'investment platforms':
                    tag_name = 'investment-app-user'
                else:
                    tag_name = 'non-online-banking-user'

            # question 7: Which work or school-related tools do you use frequently?
            elif question_id == 26:
                if answer_text.lower() == 'microsoft office 365':
                    tag_name = 'microsoft-tools-user'
                elif answer_text.lower() == 'google workspace':
                    tag_name = 'google-tools-user'
                elif answer_text.lower() == 'zoom':
                    tag_name = 'zoom-user'
                elif answer_text.lower() == 'slack':
                    tag_name = 'slack-user'
                elif answer_text.lower() == 'microsoft teams':
                    tag_name = 'microsoft-teams-user'
                else:
                    tag_name = 'other-work-school-tools-user'

            # question 8: What type of email are you most likely to open immediately?
            elif question_id == 27:
                if answer_text.lower() == 'work/school related':
                    tag_name = 'work-school-email-priority'
                elif answer_text.lower() == 'personal correspondence':
                    tag_name = 'personal-email-priority'
                elif answer_text.lower() == 'shopping/retail':
                    tag_name = 'shopping-email-priority'
                elif answer_text.lower() == 'financial notifications':
                    tag_name = 'financial-email-priority'
                elif answer_text.lower() == 'social media notifications':
                    tag_name = 'social-media-email-priority'
                else:
                    tag_name = 'generic-email-priority'

            # question 9: Which social media services do you use?
            elif question_id == 28:
                if answer_text.lower() == 'facebook':
                    tag_name = 'facebook-user'
                elif answer_text.lower() == 'instagram':
                    tag_name = 'instagram-user'
                elif answer_text.lower() == 'twitter':
                    tag_name = 'twitter-user'
                elif answer_text.lower() == 'linkedin':
                    tag_name = 'linkedin-user'
                elif answer_text.lower() == 'snapchat':
                    tag_name = 'snapchat-user'
                elif answer_text.lower() == 'tiktok':
                    tag_name = 'tiktok-user'
                else:
                    tag_name = 'non-social-media-user'
                    
            elif question_id == 29:
                if answer_text.lower() == 'n/a':
                    tag_name = 'unemployed'
                else:
                    tag_name = 'employed'
                    
            

            if tag_name:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.session.add(tag)
                    db.session.flush()
                 
                if tag:
                    tags_to_add.append(tag)
                    
        for tag in tags_to_add:
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

class PeerPhishingTemplate(db.Model):
    """
    Represents a phishing template that is sent by a student to another student
    
    Args:
        db (_type_): _description_
    """
    __tablename__ = "peer_phishing_templates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(250))
    difficulty_level = db.Column(Enum(DifficultyLevel), nullable=False)
    sender_template = db.Column(db.String(120), nullable=False)
    subject_template = db.Column(db.String(120), nullable=False)
    body_template = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(100))
    template_redflag=db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    
    phishing_emails = db.relationship("PhishingEmail", back_populates="peer_phishing_template", lazy=True)
    tags = db.relationship("Tag", secondary="peer_phishing_template_tags", back_populates="peer_phishing_templates")
    
    def serialize(self):
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
            'template_redflag': self.template_redflag,
            'created_by': self.created_by
        }



class PeerPhishingTemplateTags(db.Model):
    """Association table for many-to-many relationship between PeerPhishingTemplate and Tag

    Args:
        db (_type_): _description_
    """
    __tablename__ = "peer_phishing_template_tags"
    template_id = db.Column(db.Integer, db.ForeignKey('peer_phishing_templates.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def serialize(self):
        """
        Convert model of a peer phishing template tag into a serializable dictionary
        """
        return {
            'template_id': self.template_id,
            'tag_id': self.tag_id
        }

class TargetList(db.Model):
    """ Represents a list of targets for a phishing campaign

    Args:
        db (_type_): _description_
    """
    __tablename__ = "target_lists"
    id = db.Column(db.Integer, primary_key=True)
    student_profile_id = db.Column(db.Integer, db.ForeignKey('student_profiles.id'), nullable=False)
    
    student_profile = db.relationship("StudentProfile", back_populates="target_list")
    
    def serialize(self):
        """
        serialize the target list model
        
        """
        return {
            'id': self.id,
            'student_profile_id': self.student_profile_id
        }
        
    @classmethod
    def filter_available_peer_phishing_targets(cls):
        """
        Filter the target list to only include students who have not been 
        recipients of a phishing email created by a peer phishing template.
        
        Returns:
            list: A list of TargetList objects representing student profiles that are available as targets.
        """
        targeted_recipients_subquery = (
            db.session.query(PhishingEmail.recipient)
            .filter(PhishingEmail.peer_phishing_template_id.isnot(None))
            .subquery()
        )
        
        # Filter available targets
        available_targets = (
            db.session.query(cls)
            .join(StudentProfile)
            .filter(~StudentProfile.email_used_for_platforms.in_(targeted_recipients_subquery))
            .all()
        )
        
        return available_targets
