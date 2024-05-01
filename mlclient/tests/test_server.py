
import pytest
from unittest.mock import MagicMock, patch
from io import BytesIO
from PIL import Image
import numpy as np
import sys
sys.path.append('mlclient')

# test
# from server import app

# @pytest.fixture
# def client():
#     """ensure flask was set up correctly"""
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_home_route(client):
#     """ensure the homepage is accessible"""
#     response = client.get('/')
#     assert response.status_code == 200

# if __name__ == '__main__':
#     pytest.main()