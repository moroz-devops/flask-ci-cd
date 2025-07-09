import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_status_page():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
