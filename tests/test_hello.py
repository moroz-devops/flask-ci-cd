import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_hello_get():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert b"Enter your name" in response.data
    
def test_hello_post():
    client = app.test_client()
    response = client.post('/hello', data={'name': 'Petro'})
    assert response.status_code == 200
    assert b"Hello, Petro!" in response.data
