from flask import Blueprint, request, jsonify, redirect
from backend.project import db
from database.models.template import Template, DifficultyLevel, Tag
from database.models.phishing_email import PhishingEmail


phishing_templates = Blueprint("phishing_templates", __name__)

@phishing_templates.route('/templates', methods=['GET'])
def get_templates():
    """
    logic for retrieving all templates
    """
    if request.method == 'GET':
        templates = Template.query.all()
        return jsonify({
            'success': True,
            'templates': [template.serialize() for template in templates]
        }), 200

@phishing_templates.route('/templates/<template_id>', methods=['GET'])
def get_template(template_id):
    """
    logic for retrieving a specific template

    Args:
        template_id (int): unique identifier for the phishing template.
    """
    if request.method == 'GET':
        template = Template.query.get(template_id)
        if not template:
            return jsonify(message="Template not found!"), 404
        return jsonify({
            'success': True,
            'template': template.serialize()
        }), 200

@phishing_templates.route('/templates', methods=['POST'])
def create_template():
    """
    logic for creating a new phishing template.
    """
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        category = data.get('category')
        tag_names = data.get('tags')
        difficulty_level_str = data.get('difficulty_level')
        sender_template = data.get('sender_template')
        subject_template = data.get('subject_template')
        body_template = data.get('body_template')
        link = data.get('link')
        template_redflag = data.get('template_redflag')
        
       
        
        existing_templates = Template.query.filter_by(name=name).first()
        if existing_templates:
            return jsonify(message="Template name already exists!"), 409
        
        try:
            difficulty_level = DifficultyLevel[difficulty_level_str]  # Convert string to enum
        except KeyError:
            return jsonify(message="Invalid difficulty level!"), 400
        
        tag_objects = []
        if tag_names:
            for tag_name in tag_names:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)  # Create a new tag if it doesn't exist
                    db.session.add(tag)
                tag_objects.append(tag)
        
        template = Template(
                name = name,
                description=description,
                category = category,
                difficulty_level=difficulty_level,
                sender_template=sender_template,
                subject_template=subject_template,
                body_template=body_template,
                link=link,
                template_redflag=template_redflag,
                tags=tag_objects
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
    """
    logic for deleting a phishing template.
    Args:
        template_id (_type_): _description_
    """
    if request.method == 'DELETE':
        template = Template.query.get(template_id)
        if not template:
            return jsonify(message="Template not found!"), 404
        db.session.delete(template)
        db.session.commit()
        return jsonify(message="Template deleted successfully!"), 200
    
@phishing_templates.route('/track/<int:email_id>', methods=['GET'])
def track_link(email_id):
    """
    Endpoint to track when a phishing link is clicked.
    """
    email = PhishingEmail.query.get(email_id)
    if not email:
        return jsonify({'error': 'Invalid email ID'}), 404

    # Update the tracking information
    email.is_link_clicked = True
    db.session.commit()

    # Redirect the user to the original link (optional)
    template = email.template
    original_link = template.link if template else '/'
    return redirect(original_link)
