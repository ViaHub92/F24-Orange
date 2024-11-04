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
        
def test_questionnaire_creation(client):
    """ Test creating a new questionnaire

    Args:
        client (_type_): Flask test client
    """
    new_questionnaire = { 
        "name": "Test Questionnaire",
        "description": "A test questionnaire",
        'questions': [
            {
                'question_text': 'Are you Employed?',
                'question_type': 'True/False'
            },
            {
                'question_text': 'How many times a day do you check your email?',
                'question_type': 'multiple choice'
            }
        ]      
    }
    response = client.post('/questionnaire', json=new_questionnaire)
    assert response.status_code == 200
    assert response.json['name'] == 'Test Questionnaire'
    assert response.json['description'] == 'A test questionnaire'
    assert len(response.json['questions']) == 2
   