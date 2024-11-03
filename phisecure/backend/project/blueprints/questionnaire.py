from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.questionnaire import Questionnaire
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
      
      existing_questionnaire = Questionnaire.query.filter_by(name=name).first()
      if existing_questionnaire:
          return jsonify(message="Questionnaire name already exists!"), 409
        
    new_questionnaire = Questionnaire(name=name)
    db.session.add(new_questionnaire)
    db.session.commit()
    return jsonify({
        'success': True,
        'questionnaire': new_questionnaire.serialize()
    }), 201