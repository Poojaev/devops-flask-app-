import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app  # Now this should work correctly

def test_home():
    tester = app.app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data
