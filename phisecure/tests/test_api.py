import pytest
from backend.project import create_app, db  # Import from your __init__.py
from flask import Flask

@pytest.fixture
def app():
    # Use your create_app function to initialize the Flask app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests

    with app.app_context():
        db.create_all()  # Create all tables in the test database
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # Create a test client using the app fixture
    return app.test_client()

import pytest
from backend.project import create_app, db
from database.models.user import User
from flask import jsonify

@pytest.fixture
def app():
    # Use your create_app function to initialize the Flask app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests

    with app.app_context():
        db.create_all()  # Create all tables in the test database
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # Create a test client using the app fixture
    return app.test_client()

def test_account(client):
    """Test creating a user."""
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password_hash": "hashed_password",
        "first_name": "Test",
        "last_name": "User"
    }
    create = client.post('/account/create_user', json=user_data)
    assert create.status_code == 201, "User creation failed"
    assert b"User created successfully!" in create.data
    get = client.get('/account/get_user/testuser')
    assert get.status_code == 200
    user_info = get.get_json()
    assert user_info["username"] == "testuser"
    assert user_info["email"] == "testuser@example.com"
    list_test = client.get('account/list_users', json=user_data)
    assert list_test.status_code == 200
    users_list = list_test.get_json()
    assert len(users_list) > 0
    assert users_list[0]["username"] == "testuser"