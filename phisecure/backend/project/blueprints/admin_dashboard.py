from flask import Blueprint, request, jsonify, session, redirect
from backend.project import db
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.email import Email
from database.models.course import Course
from database.models.role import Role
from database.models.inbox import Inbox
from database.models.phishing_email import PhishingEmail
from database.models.user_interaction import UserInteraction
from datetime import datetime, timezone

admin_dashboard = Blueprint('admin_dashboard', __name__)

#Get the amount of emails sent in total, and which ones performed the best and worst
@admin_dashboard.route('/email_total_report', methods=['POST'])
def email_total_report():
    email_total = 0
    students = Student.query.all()
    if students:
        for student in students:
            inbox_emails = Email.query.filter_by(recipient=student.email).all()
            inbox_phishing_emails = PhishingEmail.query.filter_by(recipient=student.email).all()
            for email in inbox_emails:
                email_total += 1
            for email in inbox_phishing_emails:
                email_total += 1
        report = {
            "Total Emails": email_total
        }
        return jsonify(report), 200
    else:
        return jsonify({"message": "No students found"}), 404

#Get the amount of emails sent on a certain date
@admin_dashboard.route('/email_date_total_report', methods=['POST'])
def email_date_total_report(rdate):
    email_total = 0
    # rdate = rdate.date()
    students = Student.query.all()
    if students:
        for student in students:
            inbox_emails = Email.query.filter_by(recipient=student.email, sent_at=rdate).all()
            inbox_phishing_emails = PhishingEmail.query.filter_by(recipient=student.email, sent_at=rdate).all()
            for email in inbox_emails:
                email_total += 1
            for email in inbox_phishing_emails:
                email_total += 1
        report = {
            "Total Emails": email_total
        }
        return jsonify(report), 200
    else:
        return jsonify({"message": "No students found"}), 404

#Get statistics from student profiles
@admin_dashboard.route('/student_comparison_report', methods=['POST'])
def student_comparison_report():
    return jsonify({"message": "CURRENTLY NOT IMPLEMENTED. BLAME HUNTER. :)"}), 400

#Get statistics from student profiles based on major
@admin_dashboard.route('/student_comparison_major_report', methods=['POST'])
def student_comparison_major_report(major):
    return jsonify({"message": "CURRENTLY NOT IMPLEMENTED. BLAME HUNTER. :)"}), 400
