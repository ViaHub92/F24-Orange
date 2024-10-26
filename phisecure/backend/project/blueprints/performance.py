from flask import Blueprint, jsonify
from backend.project import db
from database.models.email import Email
from database.models.student import Student
from database.models.user_interaction import UserInteraction
from datetime import datetime

performance = Blueprint('performance', __name__)

@performance.route('/<int:student_id>', methods=['GET'])
def performance_report(student_id):
    # Get all student interactions
    interactions = UserInteraction.query.filter_by(student_id=student_id).all()
    print(f"Interactions for student {student_id}: {interactions}")
    # Initialize a report dictionary
    report = []

    for interaction in interactions:
        student = Student.query.get(interaction.student_id)
        email = Email.query.filter_by(id=interaction.email_id).first()
        
        print(f"Processing interaction: {interaction}, Student: {student}, Email: {email}")

        if student and email:
            report.append({
                "student_id": student.id,
                "student_email": student.email,
                "email_subject": email.subject,
                "opened": interaction.opened,
                "link_clicked": interaction.link_clicked,
                "replied": interaction.replied,
                "template_id": interaction.template_id
            })

    return jsonify(report), 200