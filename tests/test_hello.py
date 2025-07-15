import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from flask_sqlalchemy import SQLAlchemy

def test_hello_get():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert b"Register" in response.data

def test_hello_post_new_user():
    client = app.test_client()
    response = client.post("/hello", data={"name": "UniqueUser123"})
    assert response.status_code == 200
    assert b"registered" in response.data

def test_hello_post_existing_user():
    client = app.test_client()

    # Перший запит — реєстрація
    client.post("/hello", data={"name": "DuplicateUser"})

    # Повторний запит — має показати, що ім'я вже є
    response = client.post("/hello", data={"name": "DuplicateUser"})
    assert response.status_code == 200
    assert b"is already registered" in response.data
    
def test_hello_post_invalid_name():
    client = app.test_client()
    response1 = client.post("/hello", data={"name": ""})
    assert "cannot be empty" in response1.data.decode('utf-8')

    response2 = client.post("/hello", data={"name": "ab"})
    assert "3–20 characters" in response2.data.decode('utf-8')
