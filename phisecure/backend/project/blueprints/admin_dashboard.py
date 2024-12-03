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
from database.models.template import StudentProfile
from datetime import datetime, timezone

admin_dashboard = Blueprint('admin_dashboard', __name__)

#Grab all the tags currently in the database
@admin_dashboard.route('/get_tags', methods=['GET'])
def get_tags():
    students = Student.query.all()
    if students:
        student_ids = [student.id for student in students]
        student_profiles = StudentProfile.query.filter(StudentProfile.student_id.in_(student_ids)).all()
        tags = [tag.name for profile in student_profiles for tag in profile.tags]
        tags = list(set(tags))
        return jsonify(tags), 200
    else:
        return jsonify({"message": "No students found"}), 404

#Get the amount of emails sent in total, and which ones performed the best and worst
@admin_dashboard.route('/email_total_report', methods=['POST'])
def email_total_report():
    students = Student.query.all()
    if students:
        for student in students:
            email_total = 0
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
    students = Student.query.all()
    if students:
        #Grab the data needed for analysis
        percentages = []
        student_ids = [student.id for student in students]
        student_profiles = StudentProfile.query.filter(StudentProfile.student_id.in_(student_ids)).all()
        tags = [tag.name for profile in student_profiles for tag in profile.tags]
        amntOfStudents = len(student_profiles)
        tags = list(set(tags))
        
        #For each tag, get the percentage of how much they appear in student profiles and append them to percentages
        for tag in tags:
            for student_profile in student_profiles:
                temp = StudentProfile.query.filter(StudentProfile.tags.any(str(tag))).all()
                percentages.append(len(temp)/len(student_profiles))
                temp = []
        res = {tags[i]: percentages[i] for i in range(len(tags))}
        return jsonify(res), 200
    else:
        return jsonify({"message", "No students found"}), 404

#Get statistics from student profiles based on major
@admin_dashboard.route('/student_comparison_major_report', methods=['POST'])
def student_comparison_major_report(major):
    students = Student.query.all()
    if students:
        #Grab the data needed for analysis
        percentages = []
        student_ids = [student.id for student in students.students]
        student_profiles = StudentProfile.query.filter(StudentProfile.student_id.in_(student_ids)).all()
        tags = [tag.name for profile in student_profiles for tag in profile.tags]
        amntOfStudents = len(student_profiles)
        tags = list(set(tags))
        
        #For each tag, get the percentage of how much they appear in student profiles and append them to percentages
        for tag in tags:
            for student_profile in student_profiles:
                temp = StudentProfile.query.filter(StudentProfile.tags.contains(tag)).all()
                percentages.append(len(temp)/len(student_profiles))
                temp = []
        res = {tags[i]: percentages[i] for i in range(len(tags))}
        return jsonify(res), 200
    else:
        return jsonify({"message", "No students found"}), 404
