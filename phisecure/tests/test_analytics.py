import pytest
from backend.project import create_app, db
from database.models.course import Course
from database.models.student import Student
from database.models.instructor import Instructor
from database.models.phishing_email import PhishingEmail
from database.models.template import Template
from database.models.user_interaction import UserInteraction
from backend.config import TestConfig

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def create_sample_data():
     # Create an instructor
    instructor = Instructor(id=1, username="instructor1", email="instructor1@example.com", password_hash="hashed_password")
    db.session.add(instructor)
    db.session.commit()
     # Create a course
    course = Course(id=1, course_name="Test Course", instructor_id=1)
    db.session.add(course)
    db.session.commit()

    # Create students
    student1 = Student(id=1, username="student1", email="student1@example.com", password_hash="hashed_password1", inbox_id=1, role_id=1, course_id=1)
    student2 = Student(id=2, username="student2", email="student2@example.com", password_hash="hashed_password2", inbox_id=2, role_id=1, course_id=1)
    db.session.add_all([student1, student2])
    db.session.commit()

    # Create a template
    template = Template(id=1, name="Test Template", description="Test", category="Test", difficulty_level="beginner", sender_template="sender@example.com", subject_template="Test Subject", body_template="Test Body")
    db.session.add(template)
    db.session.commit()

    # Create phishing emails
    email1 = PhishingEmail(id="1", sender="phisher@example.com", recipient="student1@example.com", subject="Test Email 1", body="This is a test email.", inbox_id=1, template_id=1)
    email2 = PhishingEmail(id="2", sender="phisher@example.com", recipient="student2@example.com", subject="Test Email 2", body="This is another test email.", inbox_id=2, template_id=1)
    db.session.add_all([email1, email2])
    db.session.commit()

    # Create user interactions
    interaction1 = UserInteraction(id=1, student_id=1, phishing_email_id="1", opened=True, link_clicked=True, replied=False)
    interaction2 = UserInteraction(id=2, student_id=2, phishing_email_id="2", opened=True, link_clicked=False, replied=True)
    db.session.add_all([interaction1, interaction2])
    db.session.commit()

def test_get_analytics(client):
    create_sample_data()
    response = client.get('/instructor_dashboard/analytics/1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['template_id'] == 1
    assert data[0]['template_name'] == "Test Template"
    assert data[0]['total_opened'] == 2
    assert data[0]['total_links_clicked'] == 1
    assert data[0]['total_replied'] == 1
    assert data[0]['total_phishing_emails'] == 2
    assert data[0]['open_rate'] == 100.0
    assert data[0]['click_rate'] == 50.0
    assert data[0]['reply_rate'] == 50.0
    