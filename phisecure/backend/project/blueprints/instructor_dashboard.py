from flask import Blueprint, request, jsonify, session, redirect
from backend.project import db
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.course import Course
from database.models.role import Role
from database.models.inbox import Inbox
from database.models.phishing_email import PhishingEmail
from database.models.user_interaction import UserInteraction
from database.models.template import StudentProfile, Template
from datetime import datetime, timezone
from collections import Counter

instructor_dashboard = Blueprint('instructor_dashboard', __name__)


#Grab a list of students from an course
@instructor_dashboard.route('/list_course_students/<int:course_id>', methods=['GET'])
def list_course_students(course_id):
    course = db.session.get(Course, course_id)
    
    if not course:
        return jsonify({"message": "Course not found."}), 404
    
    students = Student.query.filter_by(course_id=course_id)
    if students:
        student_list = [{
            "username": student.username,
            "email": student.email,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "student_id": student.id
        } for student in students]
        return jsonify(student_list), 200
    else:
        return jsonify({"message": "No students found in course"}), 404

#Grab all the courses an instructor instructs
@instructor_dashboard.route('/list_instructor_courses/<int:instructor_id>', methods=['POST'])
def list_instructor_courses(instructor_id):
    courses = Course.query.filter_by(instructor_id=instructor_id)
    
    if courses:
        course_list = [{
            "id": course.id,
            "course_name": course.course_name
        } for course in courses]
        return jsonify(course_list), 200
    else:
        return jsonify({"message": "No courses attributed to instructor"}), 404


#Create a report from all students in a class about their performance
@instructor_dashboard.route('/get_class_performance_data/<int:course_id>', methods=['GET'])
def get_class_performance_data(course_id):
    course = Course.query.filter_by(id=course_id).first()
    redirect_string = "/summary"
    
    if not course:
        return jsonify({"message": "Course not found."}), 404
    
    if course:
        summary_report_list = []
        for student in course.students:
            interactions = UserInteraction.query.filter_by(student_id=student.id).all()
            student = Student.query.get(student.id)

            if not student:
                return jsonify({"error": "Student not found"}), 404

            total_opened = sum(1 for interaction in interactions if interaction.opened)
            total_replied = sum(1 for interaction in interactions if interaction.replied)
            total_links_clicked = sum(1 for interaction in interactions if interaction.link_clicked)

            summary_report = {
                "student_id": student.id,
                "student_name": student.username,
                "total_opened": total_opened,
                "total_replied": total_replied,
                "total_links_clicked": total_links_clicked,
                "total_interactions": len(interactions),
            }
            summary_report_list.append(summary_report)
        return jsonify(summary_report_list), 200
    else:
        return jsonify({"message": "No students in course."}), 404
    
@instructor_dashboard.route('/phishing_email/<email_id>/feedback', methods=['PATCH'])
def leave_feedback(email_id):
    """
    Allows an instructor to leave feedback on a phishing email.
    
    Args:
    email_id: The ID of the phishing email to be updated.

    Request JSON:
    {
        "instructor_feedback": "Detailed feedback or comment on the email."
    }
    
    Returns:
    Success: 200 with the updated email details.
    Failure: 404 if email is not found, 400 for invalid input.
    """
    data = request.get_json()
    feedback = data.get('instructor_feedback')

    if not feedback:
        return jsonify({'error': 'Instructor feedback is required.'}), 400

    phishing_email = PhishingEmail.query.get(email_id)
    if not phishing_email:
        return jsonify({'error': 'Phishing email not found.'}), 404

    phishing_email.instructor_feedback = feedback
    db.session.commit()

    return jsonify({
        'email_id': phishing_email.id,
        'recipient': phishing_email.recipient,
        'subject': phishing_email.subject,
        'instructor_feedback': phishing_email.instructor_feedback,
        'updated_at': datetime.now(timezone.utc).isoformat()
    }), 200

@instructor_dashboard.route('/common_tag/<int:course_id>', methods=['GET'])
def common_tag(course_id):
    """
    Provides the most common tag shared by the class
    
    Args:
        course_id: ID of the course.
    
    Returns:
        A JSON object containing the most common tag and the most successful template.
    """
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    student_ids = [student.id for student in course.students]
    student_profiles = StudentProfile.query.filter(StudentProfile.student_id.in_(student_ids)).all()

    tags = [tag.name for profile in student_profiles for tag in profile.tags]
    most_common_tag = Counter(tags).most_common(1)
    most_common_tag = most_common_tag[0][0] if most_common_tag else None

    return jsonify({
        "most_common_tag": most_common_tag,
    }), 200

@instructor_dashboard.route("/most_successful_template/<int:course_id>", methods=["GET"])
def get_most_successful_template(course_id):
    """
    Endpoint to get the most successful phishing email template based on interaction rate for a specific course.
    
    Args:
        course_id (int): The ID of the course.
        
    Returns:
        JSON response containing the most successful template and interaction data.
    """
    course = Course.query.get(course_id)
    
    if not course:
        return jsonify({"error": "Course not found"}), 404
    
    students = course.students
    
    if not students:
        return jsonify({"error": "No students found for this course"}), 404
    
    phishing_emails = PhishingEmail.query.filter(PhishingEmail.inbox_id.in_([student.inbox_id for student in students])).all()

    if not phishing_emails:
        return jsonify({"error": "No phishing emails found for this course"}), 404
    
    interaction_rates = Template.calculate_interaction_rate()
    
    if not interaction_rates:
        return jsonify({"error": "No interaction data available for the templates"}), 404
    
    most_successful_template = max(interaction_rates, key=lambda x: x['interaction_rate'])
    
    template = Template.query.get(most_successful_template['template_id'])
    
    if not template:
        return jsonify({"error": "Template not found"}), 404
    
    return jsonify({
        "template_id": most_successful_template['template_id'],
        "template_name": most_successful_template['template_name'],
        "subject": template.subject_template,
        "body": template.body_template,
        "total_interactions": most_successful_template['total_interactions'],
        "total_opened": most_successful_template['total_opened'],
        "total_links_clicked": most_successful_template['total_links_clicked'],
        "total_replied": most_successful_template['total_replied'],
        "interaction_rate": most_successful_template['interaction_rate']
    })
