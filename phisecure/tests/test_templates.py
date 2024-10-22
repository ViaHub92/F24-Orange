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
    pass