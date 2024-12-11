from flask import Blueprint, request, jsonify, session
from backend.project import db, login_manager
from flask_login import login_user
from flask_login import logout_user
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.course import Course
from database.models.role import Role
from database.models.inbox import Inbox
from database.models.admin import Admin
from database.models.template import StudentProfile

account = Blueprint('account', __name__)

@login_manager.user_loader
def load_user(user_id):
    user = Student.query.get(int(user_id)) or Instructor.query.get(int(user_id))
    return user
#Create a new student
@account.route('/create_student', methods=['POST'])
def create_student():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    course_id = data.get('course_id')

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
        inbox_id=inbox.id,
        course_id=course_id
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


    # Create new instructor
    new_instructor = Instructor(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    
    new_instructor.password = password
    db.session.add(new_instructor)
    db.session.commit()

    return jsonify({"message": "Instructor created successfully!"}), 201

#Create a new admin
@account.route('/create_admin', methods=['POST'])
def create_admin():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    # Check if student already exists
    student = Admin.query.filter_by(email=email).first()
    if Admin:
        return jsonify({"message": "Admin already exists"}), 400

    # Create new admin
    new_admin = Admin(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    
    new_admin.password = password
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "admin created successfully!"}), 201


@account.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check if user is a student
    student = Student.query.filter_by(username=username).first()
    if student and student.check_password(password):
        login_user(student)
        return jsonify({'message': 'Login successful', 'role': 'Student', 'user_id': student.id}), 200
    
    # Check if user is an instructor
    instructor = Instructor.query.filter_by(username=username).first()
    if instructor and instructor.check_password(password):
        session['user_id'] = instructor.id
        session['role'] = 'Instructor'
        return jsonify({'message': 'Login successful', 'role': 'Instructor', 'user_id': instructor.id}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@account.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

#Get student data
@account.route('/get_student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = db.session.query(Student, StudentProfile).join(
        StudentProfile, Student.id == StudentProfile.student_id
    ).filter(Student.id == student_id).first()
    if student:
        student_data, profile_data = student
        return jsonify({
            "id": student_data.id,
            "username": student_data.username,
            "email": student_data.email,
            "first_name": student_data.first_name,
            "last_name": student_data.last_name,
            "course_id": student_data.course_id,
            "student_profile_id": profile_data.id
        }), 200
    else:
        return jsonify({"message": "Student not found"}), 404
    
#Get instructor data
@account.route('/get_instructor/<int:instructor_id>', methods=['GET'])
def get_instructor(instructor_id):
    instructor = Instructor.query.filter_by(id=instructor_id).first()
    if instructor:
        serialized_courses = [
            {
                "id": course.id,
                "course_name": course.course_name,
            }
            for course in instructor.courses
        ]
    if instructor:
        return jsonify({
            "id": instructor.id,
            "username": instructor.username,
            "email": instructor.email,
            "first_name": instructor.first_name,
            "last_name": instructor.last_name,
            "courses": serialized_courses
        }), 200
    else:
        return jsonify({"message": "Instructor not found"}), 404

#Get admin data
@account.route('/get_admin/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = Admin.query.filter_by(id=admin_id).first()
    if admin:
        return jsonify({
            "id": admin.id,
            "username": admin.username,
            "email": admin.email,
            "first_name": admin.first_name,
            "last_name": admin.last_name,
        }), 200
    else:
        return jsonify({"message": "Admin not found"}), 404

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
            "student_id": student.id,
            "course_id": student.course_id
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

#delete an instructor
@account.route('/delete_instructor/<int:instructor_id>', methods=['DELETE'])
def delete_student(instructor_id):
    # Find the instructor by ID
    instructor = db.session.get(Instructor, instructor_id)
    if not instructor:
        return jsonify({"message": "Instructor not found"}), 404

    # Delete the instructor
    db.session.delete(instructor)
    db.session.commit()

    return jsonify({"message": "Instructor deleted successfully!"}), 200