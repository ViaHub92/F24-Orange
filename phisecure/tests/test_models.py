from datetime import datetime, timezone
import pytest
from database.models import Role, Inbox, Email, Course, Student, Instructor, Admin, Template, DifficultyLevel
from backend.project import create_app, db
from backend.config import TestConfig




"""
class TestConfig:
    
    Configuration for Flask testing.

    Sets up an in-memory SQLite database

    Attributes:
    SQLALCHEMY_DATABASE_URI (str): URI for the SQLite database.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disables modification tracking.
    TESTING (bool): Enables testing mode.
    

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
"""


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
    # db.drop_all()


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

        # Create a Student User
        new_user = Student(
            username="testuser",
            email="testuser@phisecure.com",
            first_name="Test",
            last_name="User",
            inbox_id=user_inbox.id,  # Use generated inbox ID
            role_id=role.id,  # Use generated role ID
        )
        
        # hash the password for user using bcrypt
        new_user.password = "password12345"
      
        
        db_session.add(new_user)
        db_session.commit()

        get_user = Student.query.filter_by(username="testuser").first()
        is_hashed = get_user.check_password("password12345")
       
        assert get_user is not None
        assert get_user.inbox_id == 1
        assert is_hashed

       

    def test_email_creation(self, db_session):
        """
        Test that an email is created with all fields which include
        sender, recipient, subject, body, timestamp, and inbox

        Args:
            db_session (Session): A SQLAlchemy session object used to interact with the database.
        """

        student_user_inbox = Inbox()
        db_session.add(student_user_inbox)
        db_session.commit()

        test_email = Email(
            sender="Mrbeans@gmail.com",
            recipient="student_user@gmail.com",
            sent_at=datetime(2024, 10, 11, 15, 30, tzinfo=timezone.utc),
            subject="CS411 Meeting Reminder",
            body="Don't forget about the meeting tomorrow",
            inbox_id=student_user_inbox.id,
        )
        db_session.add(test_email)
        db_session.commit()

        get_test_email = Email.query.get(1)

        assert get_test_email is not None
        assert get_test_email.sent_at is not None
        assert get_test_email.id == 1
        assert get_test_email.sender == "Mrbeans@gmail.com"
        assert get_test_email.recipient == "student_user@gmail.com"
        assert get_test_email.subject == "CS411 Meeting Reminder"
        assert get_test_email.body == "Don't forget about the meeting tomorrow"

    
    def test_create_and_read_phishing_template(self, db_session):
        """
        Test the creation of a new phishing template in the database.

         Args:
        db_session (Session): A SQLAlchemy session object used to interact with the database.
        """
        
         # Create a role
        role = Role(name="student")
        db_session.add(role)
        db_session.commit()
        
        
        student_user_inbox = Inbox()
        db_session.add(student_user_inbox)
        db_session.commit()
        
        new_user = Student(
            username="testuser",
            email="testuser@phisecure.com",
            first_name="Test",
            last_name="User",
            inbox_id=student_user_inbox.id, 
            role_id=role.id,  
        )
        
        # hash the password for user using bcrypt
        new_user.password = "password12345"
        db_session.add(new_user)
        db_session.commit()

        
        phishing_template = Template(
            name="Test Phishing Template",
            description="Test Description",
            category="Test Category",
            subject="Test Subject",
            body="this is a tester",
            tags = "Test Tags",
            difficulty_level=DifficultyLevel.beginner,
            sender="phisher350@gmail.com",
            recipient= new_user.email,
            link="www.testlink.com")
        db_session.add(phishing_template)
        db_session.commit()
        
        test_phishing_template_email = Email(
            sender=phishing_template.sender,
            recipient=phishing_template.recipient,
            sent_at=datetime(2024, 10, 11, 15, 30, tzinfo=timezone.utc),
            subject=phishing_template.subject,
            body=phishing_template.body,
            inbox_id=student_user_inbox.id,
        )
        db_session.add(test_phishing_template_email)
        db_session.commit()
    
    
    def test_get_all_phishing_templates(self, db_session):
        """
        Test retrieving all phishing templates from the database.

        Args:
        db_session (Session): A SQLAlchemy session object used to interact with the database.
        """
        pass


