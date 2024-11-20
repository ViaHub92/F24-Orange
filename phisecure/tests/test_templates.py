import pytest
from database.models import Template, Tag, TemplateTag
from database.models import StudentProfile, Response, Answer, Student
from database.models import Questionnaire, Question
from backend.project import create_app, db
from backend.config import TestConfig
from datetime import datetime, timezone


@pytest.fixture(scope='session')
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        
@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def db_session(app):
    """Create a fresh database session for a test."""
    with app.app_context():
        db.session.begin_nested()
        yield db.session
        db.session.rollback()
        db.session.remove()
@pytest.fixture(scope='function')
def init_database(db_session):
    # Create the database and the database table(s)
    db.create_all()

    # Insert student data
    student = Student(username='testuser', email='testuser@example.com', first_name='Test', last_name='User', inbox_id=1, role_id=1, course_id=1)
    student.password = 'password'
    db.session.add(student)
    db.session.commit()

    # Insert questionnaire data
    questionnaire = Questionnaire(name='Test Questionnaire', description='A test questionnaire')
    db.session.add(questionnaire)
    db.session.commit()

    # Insert question data
    question = Question(questionnaire_id=questionnaire.id, question_text='Test Question', question_type='short answer')
    db.session.add(question)
    db.session.commit()

    # Insert student profile data
    student_profile = StudentProfile(
        student_id=student.id,
        first_name=student.first_name,
        email_used_for_platforms=student.email,
        employement_status="Unemployed",
        employer=None,
        risk_level="Low",
        attention_to_detail="High"
    )
    db.session.add(student_profile)
    db.session.commit()

    # Insert response data
    response = Response(questionnaire_id=questionnaire.id, student_id=student.id, student_profile_id=student_profile.id)
    db.session.add(response)
    db.session.commit()

    # Insert answer data
    answer = Answer(response_id=response.id, question_id=question.id, answer_text='')
    db.session.add(answer)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


class TestTagsWithTemplatesAndStudents:
    """Test class for tags with templates and students
    """
    def test_tag_creation(self, db_session):
        """Test tag creation
        Args:
            db_session (_type_): Database session
        """
        tag = Tag(name='Test Tag')
        db_session.add(tag)
        db_session.commit()
        assert tag.id is not None, "Tag created successfully"
        
   

def test_phishing_template(client):
    """ Test creating a phishing template endpoint
    Args:
        client (_type_): Flask test client
    """
    template_data = {
        "name": "Test Phishing Template",
        "description": "Test phishing template for testing purposes",
        "category": "Test",
        "difficulty_level": "beginner",
        "sender_template": "genericemail@test.com",
        "subject_template": "Test phishing email",
        "body_template": "This is a test phishing email",
        "link": "http://test.com",
        "template_redflag": "Test red flag",
        "phishing_emails": [],
        "tags": [] 
    }
    
    response = client.post('/phishing/templates', json=template_data)
    print(response.json)
    assert response.status_code == 201, "Template created successfully"
    assert response.json['template']['name'] == template_data['name'], "Template name matches"
    assert response.json['template']['description'] == template_data['description'], "Template description matches"
    

def test_check_responses(init_database):
    """
    Test checking responses
    """
    student_profile_in_db = StudentProfile.query.first()
    student_profile_in_db_responses = student_profile_in_db.responses(questionnaire=1)
    assert student_profile_in_db_responses is not None, "Responses found"