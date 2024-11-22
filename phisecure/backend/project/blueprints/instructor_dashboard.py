from flask import Blueprint, request, jsonify, session, redirect
from backend.project import db
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.course import Course
from database.models.role import Role
from database.models.inbox import Inbox
from database.models.user_interaction import UserInteraction
import backend.project.blueprints.performance

instructor_dashboard = Blueprint('instructor_dashboard', __name__)


#Grab a list of students from an course
@instructor_dashboard.route('/list_course_students/<int:course_id>', methods=['POST'])
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
@instructor_dashboard.route('/get_class_performance_data/<int:course_id>', methods=['POST'])
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
                "student_id": student.id, #Used only for testing purposes
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