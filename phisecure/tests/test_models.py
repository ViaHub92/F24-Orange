import pytest
from database.models import Role, User, Inbox, Email, Course, Student, Instructor, Admin,Template
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

    def test_user_creation(self, db_session):
        """
        Test the creation of user with role and inbox
        """
        # Create a role
        role = Role(name="student")
        db_session.add(role)
        db_session.commit()

        # Create inbox
        user_inbox = Inbox()
        db_session.add(user_inbox)
        db_session.commit()
        
        student_course = Course(course_name="Cyber Security 101")
        db_session.add(student_course)
        db_session.commit()

        # Create a Student User
        new_user = Student(
            username="testuser",
            password_hash="hashed_password_value",
            email="testuser@phisecure.com",
            first_name="Test",
            last_name="User",
            inbox_id=user_inbox.id,  # Use generated inbox ID
            role_id=role.id,  # Use generated role ID
            course_id = student_course.id
            
        )

        db_session.add(new_user)
        db_session.commit()

        get_user = Student.query.filter_by(username="testuser").first()

        assert get_user is not None
        assert get_user.inbox_id == 1
        assert get_user.course_id == student_course.id
