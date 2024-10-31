from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.questionnaire import Questionnaire
from datetime import datetime, timezone
from backend.project.routes import routes

questionnaire = Blueprint('questionnaire', __name__)

# Route for the Questionnaire
@questionnaire.route("/sendquestionnaire")
def send_questionnaire():
    return