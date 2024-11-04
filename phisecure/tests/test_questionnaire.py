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
    """ Test creating an empty questionnaire

    Args:
        client (_type_): Flask test client
    """
    questionnaire_data = {
        'name': 'Test Questionnaire',
        'questions': []
    }
    response = client.post('/questionnaire', json=questionnaire_data)
    assert response.status_code == 201, "Questionnaire created successfully"
    assert response.json['questionnaire']['name'] == questionnaire_data['name'], "Questionnaire name matches"

def add_questions_to_questionnaire(client):
    """_summary_

    Args:
        client (_type_): _description_
    """
    