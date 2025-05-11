import app

def test_homepage():
    response = app.app.test_client().get('/')
    assert response.status_code == 200
