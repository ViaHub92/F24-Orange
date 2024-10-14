import pytest
from backend.project import create_app, db
from backend.config import TestConfig
from database.models.student import Student 

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

def test_messaging(client):
    #First, set up the dummy data for the tests
    student_data = {
        "username": "teststudent",
        "email": "teststudent@example.com",
        "password_hash": "hashed_password",
        "first_name": "Test",
        "last_name": "Student"
    }
    
    email_data = {
        "sender_email": "goofygoobers@spinglebab.net",
        "recipient_email": "teststudent@example.com",
        "subject": "Saying hi!",
        "body": "Welcome to the Crusty Knab!"
    }
    

    client.post('/account/create_student', json=student_data)
    temp = client.get('/account/get_student/teststudent')
    
    #Now, let's test grab_inbox. Since it's a new user, it SHOULD give us an empty inbox.
    grab_inbox = client.get('/messaging/inbox?student_id=temp["id"]')
    assert grab_inbox.status_code == 200, "Error in Flask endpoint."
    inbox_data = grab_inbox.get_json()
    assert not b'Student not Found' in inbox_data.data, 'Error in grabbing student data'
    assert inbox_data["inbox"].len() == 0, "Incorrect length grabbed"
    
    #Next up, test compose and view_email
    compose_email = client.post('/messaging/compose', json=student_data)
    assert compose_email.status_code == 201, "Error in Flask endpoint"
    assert b"Compose message form displayed." in compose_email.data
    
    view_email = client.get('/messaging/get_email/0')
    assert grab_inbox.status_code == 200, "Error in Flask endpoint"
    
    #Remove test student data at the end
    delete_student_info = Student.query.filter_by(username="teststudent").first()
    client.delete(f'/account/delete_student/{delete_student_info.id}') 