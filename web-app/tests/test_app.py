import pytest
import sys
sys.path.append('web-app')
from app import app
import base64
import json
from io import BytesIO

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

def test_save_picture(client):
    """Ensure the /save_picture route works"""
    #base64 string for a 1x1 pixel black png image
    fake_image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5QgFCSwYFiGXGgAAAApJREFUCNdjYGBgAAAABAABJzQnCgAAAABJRU5ErkJggg=="
    fake_image = BytesIO()
    fake_image.write(base64.b64decode(fake_image_base64))
    fake_image.seek(0)

    data = {
        'image': 'data:image/png;base64,' + base64.b64encode(fake_image.getvalue()).decode('utf-8')
    }

    #send POST request to the server
    response = client.post('/save_picture', data=data)

    #check the response
    assert response.status_code == 200, "Response status should be 200"
    assert 'Unknown Plant' in response.data.decode('utf-8'), "Check the HTML content for plant name"

