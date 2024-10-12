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

def test_account(client):
    from database.models.user import User
    
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password_hash": "hashed_password",
        "first_name": "Test",
        "last_name": "User"
    }
    
    # Test creating the user
    create = client.post('/account/create_user', json=user_data)
    assert create.status_code == 201, "User creation failed"
    assert b"User created successfully!" in create.data
    
    # Test getting the user
    get = client.get('/account/get_user/testuser')
    assert get.status_code == 200
    user_info = get.get_json()
    assert user_info["username"] == "testuser"
    assert user_info["email"] == "testuser@example.com"
    
    # Test list_users
    list_test = client.get('/account/list_users')
    assert list_test.status_code == 200
    users_list = list_test.get_json()
    assert len(users_list) > 0
    assert users_list[0]["username"] == "testuser"
    
    # Test deleting the user
    delete_user_info = User.query.filter_by(username="testuser").first()
    assert delete_user_info is not None, "User not found before deletion"
    
    delete = client.delete(f'/account/delete_user/{delete_user_info.id}')  # Use the user's ID
    assert delete.status_code == 200, "User deletion failed"
    assert b"User deleted successfully!" in delete.data

    # Test retrieving the deleted user
    get_after_delete = client.get('/account/get_user/testuser')
    assert get_after_delete.status_code == 404, "Deleted user should not be found"

    # Test trying to delete the same user again
    delete_again = client.delete(f'/account/delete_user/{delete_user_info.id}')
    assert delete_again.status_code == 404, "Should return 404 for already deleted user"
