from flask import Blueprint, request, jsonify
from backend.project import db
from database.models.template import Template



phishing_templates = Blueprint('phishing_templates', __name__)