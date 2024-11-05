from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.questionnaire import Questionnaire, Question, Response
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
        for question in data.get('questions'):
            question_text = question.get('question_text')
            question_type = question.get('question_type')
            new_question = Question(
                questionnaire=new_questionnaire, 
                question_text=question_text, 
                question_type=question_type
            )
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
        questionnaire = Questionnaire.query.get(questionnaire_id)
        if not questionnaire:
            return jsonify({"error": "Questionnaire not found"}), 404
        return jsonify(questionnaire.serialize()), 200


       
       
    
