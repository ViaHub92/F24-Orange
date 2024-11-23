import pytest
from database.models import Answer
from database.models import Student 
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
                'question_type': 'True/False',
                'options': [
                    {"option_text": "True"},
                    {"option_text": "False"}
                ]
            },
            {
                'question_text': 'How many times a day do you check your email?',
                'question_type': 'multiple choice',
                'options': [
                    {"option_text": "1"},
                    {"option_text": "2"},
                    {"option_text": "3"},
                    {"option_text": "4"},
                    {"option_text": "5+"}
                ]
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
                'question_type': 'Short answer',
                'options': []
                
                
            },
            {
                'question_text': 'Do you review links before clicking them?',
                'question_type': 'Yes or No',
                'options': [
                    {"option_text": "Yes"},
                    {"option_text": "No"}
                ]
            },
            {
                'question_text': 'Describe a time you encountered a phishing email. What did you do?',
                'question_type': 'Short answer',
                'options': []
            }
        ]      
    }
    response = client.post('/questionnaire', json=questionnaire_in_db)
    print(response.json)
    assert response.status_code == 200
    get = client.get(f'/questionnaire/{response.json["id"]}')
    assert get.status_code == 200

def test_update_questionnaire(client):
        """
        Test updating a questionnaire
        """
        # Create a new questionnaire first
        new_questionnaire = {
            "name": "Initial Questionnaire",
            "description": "Initial description",
            'questions': [
                {
                    'question_text': 'Is the earth flat?',
                    'question_type': 'true/false',
                    'options': [
                        {"option_text": "True"},
                        {"option_text": "False"}
                    ]
                }
            ]
        }
        response = client.post('/questionnaire', json=new_questionnaire)
        assert response.status_code == 200
        questionnaire_id = response.json['id']

        # Update the created questionnaire
        updated_questionnaire = {
            "name": "Updated Questionnaire",
            "description": "Updated description",
            'questions': [
                {
                    'id': response.json['questions'][0]['id'],
                    'question_text': 'Whats the capital of France?',
                    'question_type': 'multiple choice',
                    'options': [
                        {"option_text": "Berlin"},
                        {"option_text": "Paris"},
                        {"option_text": "London"},
                        {"option_text": "Madrid"}
                    ]
                },
                { #add a new question
                    'question_text': 'Are you ready to graduate?',
                    'question_type': 'yes/no',
                    'options': [
                        {"option_text": "Yes"},
                        {"option_text": "No"}
                    ]
                }
            ]
        }
        update_response = client.put(f'/questionnaire/{questionnaire_id}', json=updated_questionnaire)
        assert update_response.status_code == 200
        assert update_response.json['name'] == 'Updated Questionnaire'
        assert update_response.json['description'] == 'Updated description'
        assert len(update_response.json['questions']) == 2
        assert update_response.json['questions'][0]['question_text'] == 'Whats the capital of France?'
        assert update_response.json['questions'][1]['question_text'] == 'Are you ready to graduate?'
    
    
    
def test_submit_response(client):
    """
    Test submitting questionnaire

    Args:
        client (_type_): _description_
    """
    # Ensure the student with ID 1 exists
    student_data = {
        "username": "newuser1234",
        "email": "testuser123@gmail.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User"  
    }
    
    

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
    create = client.post('/account/create_student', json=student_data)
    response = client.post('/questionnaire/Submit/1', json=new_submission)
    assert response.status_code == 200
    
def test_retrieve_response(client):
    """
    Test retrieving a response
    """
    
    new_student_data = {
        "username": "teststudent",
        "email": "teststudent@example.com",
        "password": "hashed_password",
        "first_name": "Test",
        "last_name": "Student"
    }
    # Ensure a response with ID 1 exists
    new_response = {
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
    post_student = client.post('/account/create_student', json=new_student_data)
    client.post('/questionnaire/Submit/1', json=new_response)
    response = client.get('questionnaire/response/1')
    assert response.status_code == 200
    print(response.json)
    
    
    
    
        
class TestQuestionnaire:
    """
    test suite for the questionnaire model
    
    """

def test_analyze_answers():
    """
    Test the analyze answers method
    """
    new_submission = Answer(
        question_id=1,
        answer_text="Yes"
    )
    
    submission_data = new_submission.analyze_answers()
 
    
    print(submission_data)
    assert submission_data['question_id'] == 1
    assert submission_data['answer_text'] == "Yes"
    

