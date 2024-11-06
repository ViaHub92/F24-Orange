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
   
def test_retriveing_questionnaire(client): 
    """_summary_

    Args:
        client (_type_): _description_
    """
    questionnaire_in_db = {
        "name": "Recon Questionnaire",
        "description": "A test questionnaire",
        'questions': [
            {
                'question_text': 'Do you open all emails or skip some? Why?',
                'question_type': 'Short answer'
            },
            {
                'question_text': 'Do you review links before clicking them?',
                'question_type': 'Yes or No'
            },
            {
                'question_text': 'Describe a time you encountered a phishing email. What did you do?',
                'question_type': 'Short answer'
            }
        ]      
    }
    response = client.post('/questionnaire', json=questionnaire_in_db)
    print(response.json)
    assert response.status_code == 200
    get = client.get(f'/questionnaire/{response.json["id"]}')
    assert get.status_code == 200

def test_submit_response(client):
    """
    Test submitting questionnaire

    Args:
        client (_type_): _description_
    """
    new_submission = {
        "questionnaire_id": 1,
        "student_id": 1,
        "answers": [
            {
                "question_id": 1,
                "answer_text": "Yes"
            },
            {
                "question_id": 2,
                "answer_text": "3 times a day"
            }
        ]
    }
    response = client.post('/questionnaire/Submit', json=new_submission)
    assert response.status_code == 200
    
    