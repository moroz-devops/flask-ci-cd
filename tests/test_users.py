from app import create_app

app = create_app()

def test_users_page():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Back to main page" in response.data

