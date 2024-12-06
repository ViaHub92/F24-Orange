import pytest
from database.models import StudentProfile, PeerPhishingTemplate, Student
from database.models import PhishingEmail, UserInteraction, TargetList
from backend.project import create_app, db
from backend.config import TestConfig
from datetime import datetime, timezone
from database.models.template import DifficultyLevel

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

    # Create another student who will be the target
    target_student = Student(
        username="janedoe",
        password="password456",
        email="janedoe@example.com",
        first_name="Jane",
        last_name="Doe",
        inbox_id=2,
        role_id=1,
        course_id=1
    )
    target_student.password = "password456"  # This will hash the password
    db.session.add(target_student)
    db.session.flush()

    # Create a peer phishing template
    peer_phishing_template = PeerPhishingTemplate(
        name="Test Template",
        description="This is a test template",
        category="Test",
        difficulty_level="beginner",
        sender_template="test.sender@example.com",
        subject_template="Test Subject",
        body_template="This is the body of the test template.",
        link="http://example.com",
        template_redflag="This is a red flag",
        created_by=student.id
    )
    db.session.add(peer_phishing_template)
    db.session.flush()

    # Create a student profile
    student_profile = StudentProfile(
        student_id=target_student.id,
        first_name=target_student.first_name,
        major="Computer Science",
        email_used_for_platforms=target_student.email,
        employement_status="Employed",
        employer="Tech Corp",
        risk_level="Medium",
        attention_to_detail="High"
    )
    db.session.add(student_profile)
    db.session.flush()

    # Create a target list
    target_list = TargetList(
        student_profile_id=student_profile.id
    )
    db.session.add(target_list)
    db.session.commit()

    # Associate the target student with the student profile
    student_profile.student_id = target_student.id

    yield {
        "peer_phishing_template_id": peer_phishing_template.id,
        "student_id": student.id,
        "target_student_id": target_student.id,
        "student_profile_id": student_profile.id,
        "target_list_id": target_list.id
    }

    db.drop_all()

def test_query_peer_phishing_template(db_session, init_database):
    # Query the peer phishing template
    template = db_session.query(PeerPhishingTemplate).filter_by(name="Test Template").first()
    assert template is not None
    assert template.name == "Test Template"
    assert template.description == "This is a test template"
    assert template.category == "Test"
    assert template.difficulty_level == DifficultyLevel.beginner
    assert template.sender_template == "test.sender@example.com"
    assert template.subject_template == "Test Subject"
    assert template.body_template == "This is the body of the test template."
    assert template.link == "http://example.com"
    assert template.template_redflag == "This is a red flag"

def test_query_target_list(db_session, init_database):
    # Query the target list
    target_list = db_session.query(TargetList).first()
    assert target_list is not None
    assert target_list.student_profile_id is not None

    # Query the associated student profile
    student_profile = db_session.query(StudentProfile).filter_by(id=target_list.student_profile_id).first()
    assert student_profile is not None
    assert student_profile.first_name == "Jane"
    assert student_profile.major == "Computer Science"
    assert student_profile.email_used_for_platforms == "janedoe@example.com"
    assert student_profile.employement_status == "Employed"
    assert student_profile.employer == "Tech Corp"
    assert student_profile.risk_level == "Medium"
    assert student_profile.attention_to_detail == "High"

def test_filter_available_peer_phishing_targets(db_session, init_database):
   
   available_targets = TargetList.filter_available_peer_phishing_targets()
   
   assert available_targets is not None
   assert len(available_targets) == 1
   target_student_profile_id = init_database["student_profile_id"]
   target_found = any(target.student_profile_id == target_student_profile_id for target in available_targets)
   assert target_found