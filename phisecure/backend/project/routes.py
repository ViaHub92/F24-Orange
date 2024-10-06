from flask import Blueprint, request, jsonify
from flask import Flask 
from backend.project import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return """
    <h1>Welcome to Phisecure API</h1>
    <p>Available Routes:</p>
    <ul>
        <li><strong>/account/create_user</strong> - POST: Create a new user.</li>
        <li><strong>/account/get_user/&lt;username&gt;</strong> - GET: Manage user account by username.</li>
         <li><strong>/account/list_users</strong> - GET: List all users.</li>
    </ul>
    <p>Use POST requests to interact with the API.</p>
    """