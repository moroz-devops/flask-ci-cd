from app import app

def test_users_page():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Back to main page" in response.data

