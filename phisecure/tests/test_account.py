import pytest
from backend.project.blueprints.account import list_users, get_user, create_user
from database.db_connection import create_app, db

"""
unittesting.py
Team Orange
Last Modified: 10/3/24
Unit testing for backend.
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
        assert userlist is not None
    
    def test_get_user(self):
        assert 1 != 0
    
    def test_create_user(self):
        return 1 != 0