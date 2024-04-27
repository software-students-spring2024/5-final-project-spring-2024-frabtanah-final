import pytest
import sys
sys.path.append('web-app')
from app import app
import base64
import json

@pytest.fixture
def client():
    """ensure flask was set up correctly"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """ensure the homepage is accessible"""
    response = client.get('/')
    assert response.status_code == 200

