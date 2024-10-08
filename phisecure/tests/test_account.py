import pytest
from database.db_connection import create_app, db

"""
unittesting.py
Team Orange
Last Modified: 10/3/24
Unit testing for account and its Flask endpoints
"""

class TestConfig:
    """
    Configuration for Flask testing.

    Sets up an in-memory SQLite database

    Attributes:
    SQLALCHEMY_DATABASE_URI (str): URI for the SQLite database.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disables modification tracking.
    TESTING (bool): Enables testing mode.
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

@pytest.fixture
def client():
    """
    Provides a test client for the Flask Application.
    """
    app = create_app(TestConfig)
    app.config['TESTING'] = True
    
    with app.app_context():
        with app.test_client() as client:
            yield client


class TestAccount:
    """
    Test suite for account functions
    It tests the behavior of Account
    """
    def test_list_users(self, client):
        userlist = client.get('/list_users')
        assert userlist is not None, "Error in grabbing data from database."
    
    def test_get_user(self, client):
        user1 = client.get('/get_user/alex_johnson')
        user2 = client.get('/get_user/leedle_lee')
        assert user1 is not None and user2 is not None, "Error in grabbing data from database."
    
    def test_create_user(self, client):
        temp = client.get('/create_user')
        assert temp is not None, "Error in Flask endpoint."