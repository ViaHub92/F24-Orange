from flask import Blueprint, request, jsonify, redirect
from backend.project import db
from database.models.template import Template, DifficultyLevel, Tag, StudentProfile
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
            difficulty_level = DifficultyLevel[difficulty_level_str]
        except KeyError:
            return jsonify(message="Invalid difficulty level!"), 400
        
        tag_objects = []
        if tag_names:
            for tag_name in tag_names:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
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

@phishing_templates.route('/<int:profile_id>/tags', methods=['GET'])
def get_student_profile_tags(profile_id):
    try:
        # Query the student profile by ID
        profile = StudentProfile.query.get(profile_id)
        
        if not profile:
            return jsonify({"error": "StudentProfile not found"}), 404
        
        # Retrieve tags associated with the student profile
        tags = [tag.name for tag in profile.tags]  # Assuming `Tag` model has a `name` field

        return jsonify({"profile_id": profile_id, "tags": tags}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500