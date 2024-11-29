import pytest
from database.models.template import Template, Tag, TemplateTag
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
    questions = [
        (20,"Has your college and/or place of employment recently suffered a wide-scale spear phishing attack?", "Yes/No"),
        (21,"How often do you change your password?", "Multiple Choice"),
        (22,"Do you reuse passwords for multiple accounts?", "Yes/No"),
        (23,"Do you check the senders email address before clicking on links or replying to emails?", "Yes/No"),
        (24,"Do you shop online? If yes, which platforms do you use most?", "Multiple Choice"),
        (25,"Do you manage your finances online? Which platforms do you use?", "Multiple Choice"),
        (26,"Which work or school-related tools do you use frequently?", "Multiple Choice"),
        (27,"What type of email are you most likely to open immediately?", "Multiple Choice"),
        (28,"What social media services do you use?", "Multiple Choice"),
        (29,"Are you currently employed? if so enter the name of your employer (if your not employed simply enter N/A)", "Short Answer"),
        (30,"What is your major? (if you are undecided enter undecided)", "Short Answer")
    ]
    
    question_objects = []
    for question_id, question_text, question_type in questions:
        question = Question(id=question_id, questionnaire_id=questionnaire.id, question_text=question_text, question_type=question_type)
        db.session.add(question)
        db.session.commit()
        question_objects.append(question)

    # Insert student profile data
    student_profile = StudentProfile(
        student_id=student.id,
        first_name=student.first_name,
         major="Undeclared",
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
    answers = [
        (20, "Yes"),
        (21, "Every 3 months"),
        (22, "No"),
        (23, "Yes"),
        (24, "Amazon"),
        (25, "Banking apps"),
        (26, "Zoom"),
        (27, "Work/School related"),
        (28, "Facebook"),
        (29, "N/A"),
        (30, "Computer Science")
    ]
    
    for question_id, answer_text in answers:
        answer = Answer(response_id=response.id, question_id=question_id, answer_text=answer_text)
        db.session.add(answer)
        db.session.commit()
    
    tags = [
        "phishing-aware",
        "incident-experienced",
        "highly-security-conscious",
        "security-conscious",
        "basic-security-awareness",
        "Low-security-awareness",
        "unique-password-user",
        "link-checker",
        "link-clicker",
        "high-risk",
        "moderate-security-conscious",
        "vigilant-email-user",
        "non-vigilant-email-user",
        "phishing-unaware",
        "low-risk",
        "password-reuse",
        "amazon-shopper",
        "ebay-shopper",
        "walmart-shopper",
        "target-shopper",
        "general online shopper",
        "non-online-shopper",
        "banking-app-user",
        "paypal-user",
        "venmo-user",
        "cash-app-user",
        "zelle-user",
        "non-online-banking-user",
        "microsoft-tools-user",
        "google-tools-user",
        "zoom-user",
        "slack-user",
        "microsoft-teams-user",
        "other-work-school-tools-user",
        "work-school-email-priority",
        "personal-email-priority",
        "shopping-email-priority",
        "social-media-email-priority",
        "financial-email-priority",
        "generic-email-priority",
        "facebook-user",
        "instagram-user",
        "twitter-user",
        "linkedin-user",
        "snapchat-user",
        "tiktok-user",
        "non-social-media-user"
    ]
    
    for tag_name in tags:
        tag = Tag(name=tag_name)
        db.session.add(tag)
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
    answers = student_profile_in_db.get_answers_from_questionnaire(questionnaire_id=1)
    assert answers is not None, "Response answers found"



    
def test_get_assigned_tags_from_student_profile(init_database):
    """
    Test getting assigned tags from student profile
    """
    student_profile_in_db = StudentProfile.query.first()
    student_profile_in_db.assign_tags_to_profiles(questionnaire_id=1)
    assigned_tags = student_profile_in_db.get_assigned_tags_from_student_profile()
    
    assert len(assigned_tags) > 0, "Tags assigned to student profile"
    assert assigned_tags[0] == "phishing-aware", "First tag name matches"
    assert assigned_tags[1] == "security-conscious", "Second tag name matches"
    assert assigned_tags[2] == "unique-password-user", "Third tag name matches"
    assert assigned_tags[3] == "vigilant-email-user", "Fourth tag name matches"
    assert assigned_tags[4] == "amazon-shopper", "Fifth tag name matches"
    assert assigned_tags[5] == "banking-app-user", "Sixth tag name matches"
    assert assigned_tags[6] == "zoom-user", "Seventh tag name matches"
    assert assigned_tags[7] == "work-school-email-priority", "Eighth tag name matches"
    assert assigned_tags[8] == "facebook-user", "Ninth tag name matches"
    