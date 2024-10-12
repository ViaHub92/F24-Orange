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

def test_student_account(client):
    from database.models.student import Student  # Update the import to use Student
    
    student_data = {
        "username": "teststudent",
        "email": "teststudent@example.com",
        "password_hash": "hashed_password",
        "first_name": "Test",
        "last_name": "Student"
    }
    
    # Test creating the student
    create = client.post('/account/create_student', json=student_data)  # Adjust endpoint if necessary
    assert create.status_code == 201, "Student creation failed"
    assert b"Student created successfully!" in create.data  # Update message if needed
    
    # Test getting the student
    get = client.get('/account/get_student/teststudent')  # Adjust endpoint if necessary
    assert get.status_code == 200
    student_info = get.get_json()
    assert student_info["username"] == "teststudent"
    assert student_info["email"] == "teststudent@example.com"
    
    # Test list_students (make sure this route is created)
    list_test = client.get('/account/list_students')
    assert list_test.status_code == 200
    students_list = list_test.get_json()
    assert len(students_list) > 0
    assert students_list[0]["username"] == "teststudent"
    
    # Test deleting the student
    delete_student_info = Student.query.filter_by(username="teststudent").first()
    assert delete_student_info is not None, "Student not found before deletion"
    
    delete = client.delete(f'/account/delete_student/{delete_student_info.id}')  # Use the student's ID
    assert delete.status_code == 200, "Student deletion failed"
    assert b"Student deleted successfully!" in delete.data  # Update message if needed

    # Test retrieving the deleted student
    get_after_delete = client.get('/account/get_student/teststudent')  # Adjust endpoint if necessary
    assert get_after_delete.status_code == 404, "Deleted student should not be found"

    # Test trying to delete the same student again
    delete_again = client.delete(f'/account/delete_student/{delete_student_info.id}')
    assert delete_again.status_code == 404, "Should return 404 for already deleted student"
