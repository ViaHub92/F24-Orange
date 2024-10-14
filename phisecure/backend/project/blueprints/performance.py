from flask import Blueprint, jsonify
from backend.project import db
from database.models.email import Email
from database.models.student import Student
from datetime import datetime
from sqlalchemy import func

"""
performance.py
Team Orange
Last Modified: 10/11/24
Purpose: Aggregate data from email interaction to generate a performance report for the student.
Notes: Current form of performance.py is non-functional due to the current state of the db and messaging.py.
       Still in need of functionality to acutally monitor the emails.
"""

performance = Blueprint('performance', __name__)

class Performance:
    def __init__(self, student_id):
        self.student_id = student_id
        self.student = Student.query.get(student_id)

    def aggregate_email_data(self):
        # Get all emails received by the student
        emails = Email.query.filter_by(recipient=self.student.email).all()
        
        report_data = {
            "total_emails": len(emails),
            "opened_emails": 0,
            "replied_emails": 0,
            "clicked_links": 0,
        }
        
        for email in emails:
            # Logic to determine if the email was opened, replied, or links clicked
            if email.is_opened:
                report_data["opened_emails"] += 1
            
            if email.is_replied: #This still needs to be added to emails
                report_data["replied_emails"] += 1
            
            # If the email has links, check if any were clicked
            if email.links:  #This still needs to be added to db
                for link in email.links:
                    if link.is_clicked:
                        report_data["clicked_links"] += 1

        return report_data

    def generate_report(self):
        report_data = self.aggregate_email_data()
        report = {
            "student_id": self.student_id,
            "student_name": f"{self.student.first_name} {self.student.last_name}",
            "date": datetime.now().isoformat(),
            "performance": report_data,
        }
        
        return report

@performance.route('/<int:student_id>', methods=['GET'])
def get_performance(student_id):
    performance = Performance(student_id)
    report = performance.generate_report()
    return jsonify(report), 200