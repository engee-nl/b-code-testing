# tests/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal
from app.db.models import User
from app.core.security import verify_password

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    """Fixture for database setup and teardown."""
    db = SessionLocal()
    yield db
    db.close()

def test_signup(test_db):
    """Test user signup functionality."""
    response = client.post(
        "/api/v1/auth/signup",
        json={"username": "testuser", "password": "password123"}
    )
    assert response.status_code == 200
    assert "token" in response.json()

    # Verify the user is actually created in the database
    user = test_db.query(User).filter(User.username == "testuser").first()
    assert user is not None
    assert verify_password("password123", user.hashed_password)

def test_signin(test_db):
    """Test user signin functionality."""
    # First, ensure the user exists in the database
    test_db.add(User(username="testuser", hashed_password="password123"))
    test_db.commit()

    # Test signin
    response = client.post(
        "/api/v1/auth/signin",
        json={"username": "testuser", "password": "password123"}
    )
    assert response.status_code == 200
    assert "token" in response.json()
