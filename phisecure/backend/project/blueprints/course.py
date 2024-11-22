from flask import Blueprint, request, jsonify, session
from backend.project import db
from database.models.course import Course

course = Blueprint('course', __name__)

#List all courses
@course.route('/list_courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    if courses:
        course_list = [{
            "id": course.id,
            "course_name": course.course_name,
            "instructor_id": course.instructor_id
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
    course = Course.query.filter_by(course_name=course_name).first()
    if course:
        return jsonify({"message": "Course already exists"}), 400

    # Create new course
    new_course = Course(
        course_name=course_name,
        instructor_id=instructor_id
    )
    
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully!"}), 201

#Deletea course
@course.route('/delete_course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    # Find the Course by ID
    course = db.session.get(Course, course_id)
    if not course:
        return jsonify({"message": "Course not found"}), 404

    # Delete the Course
    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully!"}), 200

#Get course data
@course.route('/get_course/<course_name>', methods=['GET'])
def get_course(course_name):
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