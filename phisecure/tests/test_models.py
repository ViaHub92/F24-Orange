import pytest
from database.models import Role, User, Inbox, Email
from database.db_connection import create_app, db


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


@pytest.fixture(scope="module")
def app():
    """
    Provides a Flask application instance for testing.
    
    """
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="module")
def client(app):
    """
    Provides a test client for the Flask Application.
    """
    return app.test_client()


@pytest.fixture(scope="function")
def db_session(app):
    """
    Provides a database session for testing.
    """
    with app.app_context():
        db.session.begin_nested()
        yield db.session
        db.session.rollback()


class TestModels:
    """
    Test suite for database models
    It tests the behavior of entities of database.
    """

    def test_role_creation(self, db_session):
        """
        Test that the Role object in models __repr__ method
        returns the correct string representation
        """
        role = Role(name="admin")
        db_session.add(role)
        db_session.commit()

        retrieved_role = Role.query.filter_by(name="admin").first()

        # Assert that the string representation of role object matches
        assert retrieved_role is not None
        assert retrieved_role.name == "admin"
        assert role.name == "admin"

    def test_role_in_db(self, db_session):
        """
        test to see if Role is saved in database correctly and can be retrieved.
        """
        role = Role(name="student")
        db_session.add(role)
        db_session.commit()

        retrieved_role = Role.query.get(role.id)
        assert retrieved_role is not None
        assert retrieved_role.name == "student"
