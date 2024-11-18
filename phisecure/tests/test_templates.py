import pytest
from database.models import Template, Tag, TemplateTag
from backend.project import create_app, db
from backend.config import TestConfig


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
    

    