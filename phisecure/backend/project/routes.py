from flask import Blueprint, request, jsonify
from project import db
from project.models import User, Role, Inbox  # Import your models

routes = Blueprint('routes', __name__)

@routes.route('/')
def landing_page():
    return """
    <h1>Welcome to Phisecure API</h1>
    <p>Available Routes:</p>
    <ul>
        <li><strong>/create_user</strong> - POST: Create a new user.</li>
        <li><strong>/manage_account/&lt;username&gt;</strong> - GET: Manage user account by username.</li>
        <li><strong>/run_messaging</strong> - GET: Execute messaging system.</li>
    </ul>
    <p>Use POST requests to interact with the API.</p>
    """

@routes.route('/create_user', methods=['POST'])
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
        role_id=default_role.id,  # Set default role id
        inbox_id=inbox.id  # Set the created inbox id
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

@routes.route('/get_user/<username>', methods=['GET'])
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
