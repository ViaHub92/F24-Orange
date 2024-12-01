from flask import Blueprint, jsonify
from backend.project import db
from database.models.phishing_email import PhishingEmail
from database.models.student import Student
from database.models.user_interaction import UserInteraction

performance = Blueprint('performance', __name__)

@performance.route('/detailed/<int:student_id>', methods=['GET'])
def performance_report(student_id):
    """
    Gets a performance report based on student interactions with phishing_emails
    """
    interactions = UserInteraction.query.filter_by(student_id=student_id, opened=True).all()

    report = []

    for interaction in interactions:
        student = Student.query.get(interaction.student_id)
        phishing_email = PhishingEmail.query.get(interaction.phishing_email_id)

        if student and phishing_email:  
            report.append({
                "student_email": student.email,
                "email_body": phishing_email.body,
                "email_subject": phishing_email.subject,
                "opened": interaction.opened,
                "link_clicked": interaction.link_clicked,
                "replied": interaction.replied,
                "red_flag": phishing_email.red_flag,
                "instructor_feedback": phishing_email.instructor_feedback,
            })

    return jsonify(report), 200

@performance.route('/summary/<int:student_id>', methods=['GET'])
def summary_performance_report(student_id):
    """
    Gets a summary performance report aggregating the total counts for opened, replied, and link_clicked actions.
    """
    interactions = UserInteraction.query.filter_by(student_id=student_id).all()
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    total_opened = sum(1 for interaction in interactions if interaction.opened)
    total_replied = sum(1 for interaction in interactions if interaction.replied)
    total_links_clicked = sum(1 for interaction in interactions if interaction.link_clicked)

    summary_report = {
        "student_id": student.id, #Used only for testing purposes
        "student_name": student.username,
        "total_opened": total_opened,
        "total_replied": total_replied,
        "total_links_clicked": total_links_clicked,
        "total_interactions": len(interactions),
    }

    return jsonify(summary_report), 200