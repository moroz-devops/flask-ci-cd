import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

from app import app

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
    assert b"already exists" in response.data
