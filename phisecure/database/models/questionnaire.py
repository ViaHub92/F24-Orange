from backend.project import db
from sqlalchemy.orm import relationship



class Questionnaire(db.Model):
    """

    Args:
        db (_type_): _description_
    """
    
    __tablename__ = "questionnaire"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), nullable=False)
    #attribute of the Questionnaire model. it is deinfed using the relationship function that creates a realationship with Question model
    questions = relationship("Question", back_populates="questionnaire")
    
    def serialize(self):
        """
        Convert model of a questionnaire into a serializable dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
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
    #attribute of the Question model. it is deinfed using the relationship function that creates a realationship with Questionnaire model
    questionnaire = relationship("Questionnaire", back_populates="questions")
    
    responses = relationship("Response", back_populates="question")

    def serialize(self):
        """
        Convert model of a question into a serializable dictionary
        
        """
        return {
            'id': self.id,
            'questionnaire_id': self.questionnaire_id,
            'question_text': self.question_text,
            'question_type': self.question_type,
            'responses': [response.serialize() for response in self.responses]
        }
class Response(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    response_text = db.Column(db.Text, nullable=False) # For text based responses
    boolean_response = db.Column(db.Boolean, nullable=False) # For yes or no or true or false questions
    #attribute of the Response model. it is deinfed using the relationship function that creates a realationship with Question model
    question = relationship("Question", back_populates="responses")
    student = relationship("Student", back_populates="responses")
    
    def serialize(self):
        """
        Convert model of a response into a serializable dictionary
        """
        return {
            'id': self.id,
            'student_id': self.student_id,
            'question_id': self.question_id,
            'response_text': self.response_text,
            'boolean_response': self.boolean_response,
            
            
            
        }