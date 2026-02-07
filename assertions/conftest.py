from client_api.posts_api import GetPostsAPI
from client_api.client_api import ClientAPI
import pytest
import dotenv
import os

dotenv.load_dotenv()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def get_posts(base_url):
    client = ClientAPI(base_url)
    posts_api = GetPostsAPI(client)
    return posts_api