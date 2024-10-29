from backend.project import db




class Questionnaire(db.Model):
    """

    Args:
        db (_type_): _description_
    """
    
    __tablename__ = "questionnaire"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), nullable=False)
    
    questions = relationship("Question", back_populates="questionnaire")
    
    
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
    
    questionnaire = relationship("Questionnaire", back_populates="questions")
    

class Response(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    response_text = db.Column(db.Text, nullable=False) # For text based responses
    boolean_response = db.Column(db.Boolean, nullable=False) # For yes or no or true or false questions
    
    question = relationship("Question", back_populates="responses")
    