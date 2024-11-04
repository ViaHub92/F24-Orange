from backend.project import db
from sqlalchemy.orm import relationship
from datetime import datetime, timezone



class Questionnaire(db.Model):
    """

    Args:
        db (_type_): _description_
    """
    
    __tablename__ = "questionnaire"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    #attribute of the Questionnaire model. it is deinfed using the relationship function that creates a realationship with Question model
    questions = relationship("Question", back_populates="questionnaire")
    
    def serialize(self):
        """
        Convert model of a questionnaire into a serializable dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'questions': [question.serialize() for question in self.questions]
        }
    
    
class Question(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaire.id"), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(128), nullable=False) # e.g. multiple choice, short answer, etc.
    
    def serialize(self):
        """
        Convert model of a question into a serializable dictionary
        
        """
        return {
            'id': self.id,
            'questionnaire_id': self.questionnaire_id,
            'question_text': self.question_text,
            'question_type': self.question_type,
        }
class Response(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaire.id"), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    answers = relationship("Answer", back_populates="response")
    
    def serialize(self):
        """
        Convert model of a response into a serializable dictionary
        """
        return {
            'id': self.id,
            'student_id': self.student_id,
            'questionnaire_id': self.questionnaire_id,
            'submitted_at': self.submitted_at,
            'answers': [answer.serialize() for answer in self.answers]
        }

class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    response_id = db.Column(db.Integer, db.ForeignKey("response.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    answer_text = db.Column(db.Text, nullable=False)
    
    question = relationship("Question", back_populates="answers")
    
    def serialize(self):
        """
         Convert model of an answer into serializable dictionary
        """
        return {
            'id': self.id,
            'response_id': self.response_id,
            'question_id': self.question_id,
            'answer_text': self.answer_text,
            'question': self.question.serialize() if self.question else None
        }