from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from backend.project import db
from database.models.template import PeerPhishingTemplate,TargetList, PeerPhishingTemplateTags, PhishingEmail, StudentProfile
from database.models.course import Course
from database.models.inbox import Inbox
from database.models.student import Student
from datetime import datetime
from flask import current_app

peer_phishing = Blueprint('peer_phishing', __name__)



@peer_phishing.route('/fill-target-list/<int:course_id>', methods=['POST'])
def fill_target_list(course_id):
    """
    Fills the target list with students from the specified course.

    Args:
        course_id (int): ID of the course whose students will be added to the target list.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Fetch the course
        course = Course.query.get(course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404

        # Iterate through students in the course
        for student in course.students:
            # Fetch the student profile for the student
            student_profile = StudentProfile.query.filter_by(student_id=student.id).first()
            
            if not student_profile:
                continue
            
            # Check if the student profile already exists in TargetList
            existing_target = TargetList.query.filter_by(student_profile_id=student_profile.id).first()
            
            if not existing_target:
                # Add the student profile to the target list
                new_target = TargetList(student_profile_id=student_profile.id)
                db.session.add(new_target)

        db.session.commit()

        return jsonify({"message": f"Target list successfully populated for course {course.course_name}."}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    
@peer_phishing.route('/target-list', methods=['GET'])
def get_target_list():
    """
    Fetches and returns all entries in the TargetList with student_id.
    
    Returns:
        JSON response containing the serialized target list.
    """
    try:
        # Query all target list entries with associated student data
        target_list_entries = db.session.query(TargetList, Student).join(
            StudentProfile, TargetList.student_profile_id == StudentProfile.id
        ).join(
            Student, StudentProfile.student_id == Student.id
        ).all()

        # Serialize the results
        serialized_list = [{
            "target_list_id": entry[0].id,
            "student_id": entry[1].id,  # Student ID
            "student_profile_id": entry[0].student_profile_id
        } for entry in target_list_entries]

        return jsonify(serialized_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@peer_phishing.route('/target-list/course/<int:course_id>', methods=['GET'])
def get_targets_by_course(course_id):
    """
    Fetches and returns all targets for a given course.
    
    Args:
        course_id (int): ID of the course to fetch targets for.
        
    Returns:
        JSON response containing the list of targets for the course, 
        including student names and their actual IDs.
    """
    try:
        
        print(f"Fetching targets for course_id: {course_id}")
        
        targets = (
            db.session.query(TargetList, StudentProfile, Student)
            .join(StudentProfile, TargetList.student_profile_id == StudentProfile.id)
            .join(Student, StudentProfile.student_id == Student.id)
            .filter(Student.course_id == course_id)
            .all()
        )
        
        print(f"Targets fetched: {targets}")
        
        serialized_targets = [
        {
            'target_list_id': target[0].id,
            'student_id': target[2].id,
            'student_name': f"{target[2].first_name} {target[2].last_name}",
        }
        for target in targets
    ]
        
        print(f"Serialized targets: {serialized_targets}")
        
        return jsonify(serialized_targets), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@peer_phishing.route('/create-and-send', methods=['POST'])
def create_and_send_phishing_email():
    try:
        data = request.json
        
        # Create the phishing template
        new_template = PeerPhishingTemplate(
            name=data['name'],
            description=data['description'],
            category=data.get('category'),
            difficulty_level=data['difficulty_level'],
            sender_template=data['sender_template'],
            subject_template=data['subject_template'],
            body_template=data['body_template'],
            link=data.get('link'),
            template_redflag=data.get('template_redflag'),
            created_by=data['created_by']
        )
        db.session.add(new_template)
        db.session.flush()
        
        # Validate the target
        target_id = data['target_id']
        target = TargetList.query.filter_by(id=target_id).first()
        if not target:
            db.session.rollback()
            return jsonify({'error': 'Target not found or unavailable'}), 404
        
        # Retrieve the student's profile using the target's student_profile
        student_profile = StudentProfile.query.filter_by(id=target.student_profile.id).first()
        if not student_profile:
            db.session.rollback()
            return jsonify({'error': 'Student profile not found'}), 404
        
        # Retrieve the student's inbox using the student_profile's student_id
        student = Student.query.filter_by(id=student_profile.student_id).first()
        if not student:
            db.session.rollback()
            return jsonify({'error': 'Student not found'}), 404
        
        recipient_inbox = Inbox.query.filter_by(id=student.inbox_id).first()
        if not recipient_inbox:
            db.session.rollback()
            return jsonify({'error': 'Inbox not found for student'}), 404
        
        first_name = student.first_name
        link = data.get('link', '') if '{link}' in new_template.body_template else ""
        date = datetime.now().strftime("%B %d, %Y")
        try:
            body = new_template.body_template.format(
                first_name=first_name,
                link=link,
                date=date
            )
       
            subject = new_template.subject_template.format(first_name=first_name)
            
        except KeyError as e:
            return jsonify({'error': f'Missing placeholder in recipient data: {e}'}), 400
        
        # Create and send the phishing email
        phishing_email = PhishingEmail(
            sender=new_template.sender_template,
            recipient=target.student_profile.email_used_for_platforms,
            subject=new_template.subject_template,
            body=new_template.body_template,
            peer_phishing_template_id=new_template.id,
            inbox_id=recipient_inbox.id
        )
        db.session.add(phishing_email)
        db.session.commit()
        
        db.session.delete(target)
        db.session.commit()
        
        return jsonify({
            'template': new_template.serialize(),
            'email': {
                'sender': phishing_email.sender,
                'recipient': phishing_email.recipient,
                'subject': phishing_email.subject,
                'body': phishing_email.body
            },
            'message': 'Phishing template created and email sent successfully'
        }), 201
    except IntegrityError as e:
        print("IntegrityError:", str(e))
        db.session.rollback()
        return jsonify({'error': 'Template Integrity Error'}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500