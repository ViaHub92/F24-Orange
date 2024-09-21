from flask import Blueprint, request, jsonify
from flask import Flask 
from project import db
from project.models import User, Role, Inbox
from project.blueprints.account import account

routes = Blueprint('routes', __name__)

@routes.route('/')
def landing_page():
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
def register_routes(app: Flask):
    #This registers the account blueprint
    app.register_blueprint(account, url_prefix='/account')
    
    #Any other necessary blueprints can be registered here