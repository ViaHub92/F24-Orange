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
from database.models.template import StudentProfile, Template
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
        return jsonify({"message": "No tags found"}), 404
    
#Grab all the majors currently in the database
@admin_dashboard.route('/get_majors', methods=['GET'])
def get_majors():
    student_profiles = StudentProfile.query.all()
    if student_profiles:
        majors = [student_profile.major for student_profile in student_profiles]
        majors = list(set(majors))
        return jsonify(majors), 200
    else:
        return jsonify({"message": "No student profiles found"}), 404

#Get the amount of emails sent in total, and which ones performed the best and worst
@admin_dashboard.route('/email_total_report', methods=['POST'])
def email_total_report():
    students = Student.query.all()
    if students:
        #First, get the total amount of emails
        for student in students:
            email_total = 0
            inbox_emails = Email.query.filter_by(recipient=student.email).all()
            inbox_phishing_emails = PhishingEmail.query.filter_by(recipient=student.email).all()
            for email in inbox_emails:
                email_total += 1
            for email in inbox_phishing_emails:
                email_total += 1
        
        '''
        #Now, let's get the best and worst phishing template
        phishing_emails = PhishingEmail.query.all()

        if not phishing_emails:
            return jsonify({"error": "No phishing emails found for this course"}), 404
    
        rates = Template.calculate_interaction_rate()
    
        if not rates:
            return jsonify({"error": "No interaction data available for the templates"}), 404
    
        most_successful_template = max(rates, key=lambda x: (x['open_rate'], x['click_rate'], x['reply_rate']))
        least_successful_template = min(rates, key=lambda x: (x['open_rate'], x['click_rate'], x['reply_rate']))
    
        template1 = Template.query.get(most_successful_template['template_id'])
        template2 = Template.query.get(least_successful_template['template_id'])
    
        if not template1 or not template2:
            return jsonify({"error": "Template not found"}), 404
        '''
        report = {
            "Total Emails": email_total,
            #"Most Successful Template": template1,
            #"Least Successful Template": template2
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
@admin_dashboard.route('/student_comparison_report', methods=['GET'])
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
            
                temp = StudentProfile.query.filter(StudentProfile.tags.any(name=tag)).all()
                percentages.append(round((len(temp)/len(student_profiles))* 100, 2))
        res = {tags[i]: percentages[i] for i in range(len(tags))}
        return jsonify(res), 200
    else:
        return jsonify({"message": "No students found"}), 404

#Get statistics from student profiles based on major
@admin_dashboard.route('/student_comparison_major_report/<string:major>', methods=['GET'])
def student_comparison_major_report(major):
    students = Student.query.all()
    if students:
        #Grab the data needed for analysis
        percentages = []
        student_ids = [student.id for student in students]
        student_profiles = StudentProfile.query.filter(StudentProfile.student_id.in_(student_ids), StudentProfile.major == major).all()
        tags = [tag.name for profile in student_profiles for tag in profile.tags]
        amntOfStudents = len(student_profiles)
        tags = list(set(tags))
        
        #For each tag, get the percentage of how much they appear in student profiles and append them to percentages
        for tag in tags:
            temp = StudentProfile.query.filter(StudentProfile.tags.any(name=tag), StudentProfile.major == major).all()
            percentages.append(round((len(temp)/len(student_profiles))* 100, 2))
                
        res = {tags[i]: percentages[i] for i in range(len(tags))}
        return jsonify(res), 200
    else:
        return jsonify({"message", "No students found"}), 404
