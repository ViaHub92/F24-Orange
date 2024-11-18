from flask import Blueprint, request, jsonify, session
from backend.project import db
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.course import Course
from database.models.role import Role
from database.models.inbox import Inbox

"""
account.py
Team Orange
Last Modified: 10/11/24
Purpose: Creation and management of student accounts.
"""

account = Blueprint('account', __name__)

#Create a new student
@account.route('/create_student', methods=['POST'])
def create_student():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    # Check if student already exists
    student = Student.query.filter_by(email=email).first()
    if student:
        return jsonify({"message": "Student already exists"}), 400

    # Create a default role if it doesn't exist (adjust this based on your role handling)
    default_role = Role.query.first()
    if not default_role:
        default_role = Role(name='Student')
        db.session.add(default_role)
        db.session.commit()

    # Create inbox for the student
    inbox = Inbox()
    db.session.add(inbox)
    db.session.commit()

    # Create new student
    new_student = Student(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        role_id=default_role.id,
        inbox_id=inbox.id 
    )
    
    new_student.password = password
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student created successfully!"}), 201

#Create a new instructor
@account.route('/create_instructor', methods=['POST'])
def create_instructor():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    # Check if instructor already exists
    instructor = Instructor.query.filter_by(email=email).first()
    if instructor:
        return jsonify({"message": "Instructor already exists"}), 400

    # Create a default role if it doesn't exist (adjust this based on your role handling)
    default_role = Role.query.first()
    if not default_role:
        default_role = Role(name='Instructor')
        db.session.add(default_role)
        db.session.commit()

    # Create inbox for the instructor
    inbox = Inbox()
    db.session.add(inbox)
    db.session.commit()

    # Create new student
    new_instructor = Instructor(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        role_id=default_role.id,
        inbox_id=inbox.id 
    )
    
    instructor.password = password
    db.session.add(instructor)
    db.session.commit()

    return jsonify({"message": "Instructor created successfully!"}), 201



@account.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    student = Student.query.filter_by(username=username).first()
    if student and student.check_password(password):
        session['user_id'] = student.id
        session['role'] = 'Student'
        return jsonify({'message': 'Login successful', 'role': 'Student', 'user_id': student.id}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

#Get student data
@account.route('/get_student/<username>', methods=['GET'])
def get_student(username):
    student = Student.query.filter_by(username=username).first()
    if student:
        return jsonify({
            "id": student.id,
            "username": student.username,
            "email": student.email,
            "first_name": student.first_name,
            "last_name": student.last_name
        }), 200
    else:
        return jsonify({"message": "Student not found"}), 404

#List all students
@account.route('/list_students', methods=['GET'])
def list_students():
    students = Student.query.all()
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
        return jsonify({"message": "No students found"}), 404

#delete a student
@account.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Find the student by ID
    student = db.session.get(Student, student_id)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    # Delete the student
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully!"}), 200

#Grab a list of students from an course
@account.route('/list_course_students', methods=['POST'])
def list_course_students(course_id):
    course = db.session.get(Course, course_id)
    
    if not course:
        return jsonify({"message": "Course not found."}), 404
    
    students = Student.query(Student).filter(Student.course_id == course_id)
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