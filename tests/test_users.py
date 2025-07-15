from app import app
from flask_sqlalchemy import SQLAlchemy

def test_users_page():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Back to main page" in response.data

