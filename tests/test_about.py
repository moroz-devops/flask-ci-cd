import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

def test_about_page():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About this site" in response.data
    assert b"Back to main page" in response.data
