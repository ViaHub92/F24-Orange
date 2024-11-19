from flask import Blueprint, request, jsonify, session
from backend.project import db
from database.models.course import Course
from database.models.role import Role

course = Blueprint('course', __name__)

#List all courses
@course.route('/list_courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    if courses:
        course_list = [{
            "id": course.id,
            "course_name": course.course_name,
            "instructor_id": course.instructor_id,
            "students": course.students,
        } for course in courses]
        return jsonify(course_list), 200
    else:
        return jsonify({"message": "No courses found"}), 404

#Create a new course
@course.route('/create_course', methods=['POST'])
def create_course():
    data = request.json
    course_name = data.get('course_name')
    instructor_id = data.get('instructor_id')

    # Check if course already exists
    course = Course.query.filter_by(course_name).first()
    if course:
        return jsonify({"message": "Course already exists"}), 400

    # Create a default role if it doesn't exist (adjust this based on your role handling)
    default_role = Role.query.first()
    if not default_role:
        default_role = Role(name='Course')
        db.session.add(default_role)
        db.session.commit()

    # Create new course
    new_course = Course(
        id=id,
        course_name=course_name,
    )
    
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully!"}), 201

#Get course data
@course.route('/get_course/<course_name>', methods=['GET'])
def get_course(course):
    course = Course.query.filter_by(course_name=course_name).first()
    if course:
        return jsonify({
            "id": course.id,
            "course_name": course.course_name,
            "instructor_id": course.instructor_id,
            "students": course.students
        }), 200
    else:
        return jsonify({"message": "Course not found"}), 404