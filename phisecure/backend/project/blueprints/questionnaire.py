from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.questionnaire import Questionnaire, Question, Response, Answer, Option
from database.models.student import Student
from datetime import datetime, timezone
from backend.project.routes import routes

questionnaire = Blueprint('questionnaire', __name__)

# Route for the Questionnaire
@questionnaire.route("", methods=["POST"])
def create_questionnaire():
    """ 
    Route for creating a new questionnaire with no questions
    """
    if request.method == "POST":
       data = request.get_json()
       name = data.get('name')
       description = data.get('description')
    existing_questionnaire = Questionnaire.query.filter_by(name=name).first()
    if existing_questionnaire:
        return jsonify({"error": "Questionnaire with this name already exists"}), 400
    else:
        new_questionnaire = Questionnaire(name=name, description=description)
        # loop to iterate through the questions in the questionnaire
        for question in data.get('questions'):
            question_text = question.get('question_text') # get the question text
            question_type = question.get('question_type') # get the question type
            new_question = Question(
                questionnaire=new_questionnaire, 
                question_text=question_text, 
                question_type=question_type
            )
            if question_type in ["true/false", "multiple choice", "yes/no"]: #checks question type
                for option in question.get('options'): # loop to iterate through the options for the question
                    option_text = option.get('option_text')
                    new_option = Option(question=new_question, option_text=option_text)
                    db.session.add(new_option)
                    
        db.session.add(new_question)
        db.session.add(new_questionnaire)
        db.session.commit()
        return jsonify(new_questionnaire.serialize()), 200

@questionnaire.route("/<questionnaire_id>", methods=["GET"])
def get_questionnaire(questionnaire_id):
    """
    Route for retrieving a specific questionnaire
    """
    if request.method == "GET":
        found_questionnaire = Questionnaire.query.get(questionnaire_id)
        if not found_questionnaire:
            return jsonify({"error": "Questionnaire not found"}), 404
        return jsonify(found_questionnaire.serialize()), 200

@questionnaire.route("/Submit", methods=["POST"])
def submit_response():
    """
    Route for submitting a response to a questionnaire
    """
    if request.method == "POST":
        data = request.get_json()
        questionnaire_id = data.get('questionnaire_id')
        student_id = data.get('student_id')
        answers = data.get('answers')
        new_response = Response(questionnaire_id=questionnaire_id, student_id=student_id) # create a new response
        for answer in answers: # loop to iterate through the answers
            question_id = answer.get('question_id') # get the question id
            answer_text = answer.get('answer_text') # get the answer text
            new_answer = Answer(
                response=new_response, 
                question_id=question_id, 
                answer_text=answer_text
            )
            db.session.add(new_answer)
        db.session.add(new_response)
        db.session.commit()
        return jsonify(new_response.serialize()), 200
    
@questionnaire.route("/questions/<question_id>", methods=["PUT"])
def update_question(question_id):
    """
    Route for updating a question in a questionnaire
    """
    if request.method == "PUT":
        data = request.get_json()
        question_text = data.get('question_text')
        question_type = data.get('question_type')
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        question.question_text = question_text
        question.question_type = question_type
        if question_type in ["true/false", "multiple choice", "yes/no"]:
            #Clear existing options if any
            Option.query.filter_by(question_id=question_id).delete()
            
            for option in data.get('options'): # loop to iterate through the options
                option_text = option.get('option_text')
                new_option = Option(question=question, option_text=option_text)
                db.session.add(new_option)
        
        db.session.commit()
        return jsonify(question.serialize()), 200
    

       
       
    
