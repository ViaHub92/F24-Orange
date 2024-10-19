from flask import Blueprint, request, jsonify
from backend.project import db
from database.models.template import Template, DifficultyLevel


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

@phishing_templates.route('/templates', methods=['POST'])
def create_template():
    """
     Implement logic for creating a new template
    """
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        category = data.get('category')
        tags = data.get('tags')
        difficulty_level_str = data.get('difficulty_level')
        sender = data.get('sender')
        recipient = data.get('recipient')
        subject = data.get('subject')
        body = data.get('body')
        link = data.get('link', '')
        
       
        
        existing_templates = Template.query.filter_by(name=name).first()
        if existing_templates:
            return jsonify(message="Template name already exists!"), 409
        
        try:
            difficulty_level = DifficultyLevel[difficulty_level_str]  # Convert string to enum
        except KeyError:
            return jsonify(message="Invalid difficulty level!"), 400
        
        template = Template(
                name = name,
                description=description,
                category = category,
                tags=tags,
                difficulty_level=difficulty_level,
                sender=sender,
                recipient=recipient,
                subject=subject,
                body=body,
                link=link
            )
        db.session.add(template)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'template': template.serialize()
        }), 201
        
        
        

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