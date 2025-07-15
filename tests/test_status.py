import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from flask_sqlalchemy import SQLAlchemy

def test_status_page():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert b"Status: OK" in response.data
    assert b"Back to main page" in response.data
