from flask import Blueprint, request, jsonify
from backend.project import db
from database.models.user import User
from database.models.role import Role
from database.models.inbox import Inbox
"""
account.py
Team Orange
Last Modified: 9/21/24
Purpose: Creation and management of user accounts.
"""
account = Blueprint('account', __name__)

@account.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    # Check if user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "User already exists"}), 400

    # Create a default role if it doesn't exist (You might want to adjust this based on your actual role handling)
    default_role = Role.query.first()  # Assumes there is at least one role in the database
    if not default_role:
        default_role = Role(name='User')
        db.session.add(default_role)
        db.session.commit()

    # Create inbox for the user
    inbox = Inbox()
    db.session.add(inbox)
    db.session.commit()

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        first_name=first_name,
        last_name=last_name,
        role_id=default_role.id,
        inbox_id=inbox.id 
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

@account.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404

@account.route('/list_users', methods=['GET'])
def list_users():
    users = User.query.all()
    if users:
        user_list = [{
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_id" : user.id
        } for user in users]
        return jsonify(user_list), 200
    else:
        return jsonify({"message": "No users found"}), 404

@account.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Find the user by ID
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Delete the user (this will also delete the inbox if cascade is set)
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"}), 200

