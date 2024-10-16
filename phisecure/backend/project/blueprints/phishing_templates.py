from flask import Blueprint, request, jsonify
from backend.project import db
from database.models.template import Template


phishing_templates = Blueprint("phishing_templates", __name__)

@phishing_templates.route('/templates', methods=['GET'])
def get_templates():
    """
    logic for retrieving all templates
    """
    pass

@phishing_templates.route('/templates/<template_id>', methods=['GET'])
def get_template(template_id):
    """
    logic for retrieving a specific template

    Args:
        template_id (int): unique identifier for the phishing template.
    """
    pass

@phishing_templates.route('/templates', method=['POST'])
def create_template():
    """
     Implement logic for creating a new template
    """
    pass

@phishing_templates.route('/templates/<template_id>', methods=['PUT'])
def update_template(template_id):
    """_summary_

    Args:
        template_id (_type_): _description_
    """
    pass

@phishing_templates.route('/templates/<template_id>', methods=['DELETE'])
def delete_template(template_id):
    """_summary_

    Args:
        template_id (_type_): _description_
    """
    pass