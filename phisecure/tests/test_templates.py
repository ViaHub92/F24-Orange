import pytest
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
        "tags": "Test, Phishing",
        "difficulty_level": "beginner",
        "subject_template": "Test phishing email",
        "body_template": "This is a test phishing email",
        "link": "http://test.com"
    }
    
    response = client.post('/phishing/templates', json=template_data)
    print(response.json)
    assert response.status_code == 201, "Template created successfully"
    assert response.json['template']['name'] == template_data['name'], "Template name matches"
    assert response.json['template']['description'] == template_data['description'], "Template description matches"
    
   
    