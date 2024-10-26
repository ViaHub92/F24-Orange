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
        "sender": "testuser123@gmail.com",
        "recipient": "phiseduser123@gmail.com",
        "subject": "Test phishing email",
        "body": "This is a test phishing email",
        "link": "https://fakephishinglink.com"
    }
    
    response = client.post('/phishing/templates', json=template_data)
    
    assert response.status_code == 201, "Template created successfully"
    assert response.get_json()["template"]["name"] == "Test Phishing Template"
    assert response.get_json()["template"]["description"] == "Test phishing template for testing purposes"
    