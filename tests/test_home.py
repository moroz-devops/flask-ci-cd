from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"main page" in response.data
    assert b"/status" in response.data
    assert b"/about" in response.data
    assert b"/hello" in response.data
