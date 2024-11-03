from flask import Blueprint, jsonify
from backend.project import db
from database.models.phishing_email import PhishingEmail
from database.models.student import Student
from database.models.user_interaction import UserInteraction

performance = Blueprint('performance', __name__)

@performance.route('/<int:student_id>', methods=['GET'])
def performance_report(student_id):
    """
    Gets a performance report based on student interactions with phishing_emails
    """
    # Get all student interactions
    interactions = UserInteraction.query.filter_by(student_id=student_id).all()
    # Initialize a report dictionary
    report = []

    for interaction in interactions:
        student = Student.query.get(interaction.student_id)
        phishing_email = PhishingEmail.query.get(interaction.phishing_email_id)

        if student and phishing_email:  # Check against phishing_email
            report.append({
                "student_id": student.id,
                "student_email": student.email,
                "email_subject": phishing_email.subject,
                "opened": interaction.opened,
                "link_clicked": interaction.link_clicked,
                "replied": interaction.replied,
                "template_id": phishing_email.template_id
            })

    return jsonify(report), 200
