import pytest
from database.models import Template, Tag, TemplateTag, StudentTags
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
    

class TestTagsWithTemplatesAndStudents:
    """Test class for tags with templates and students
    """

def test_tag_creation(self, db_session):
    """Test creating a new tag
    Args:
        db_session (Session): A SQLAlchemy session object used to interact with the database.
    """
    tag = Tag(name="Test Tag")
    
    db_session.add(tag)
    db_session.commit()
    
    retrieved_tag = db_session.query(Tag).filter_by(name="Test Tag").first()
    
    assert retrieved_tag is not None, "Tag created successfully"
    assert retrieved_tag.name == "Test Tag", "Tag name matches"
    