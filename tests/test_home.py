import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"main page" in response.data
    assert b"/status" in response.data
    assert b"/about" in response.data
    assert b"/hello" in response.data
    assert b"/users" in response.data
