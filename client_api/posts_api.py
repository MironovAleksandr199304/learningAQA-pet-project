from client_api.endpoints import *

posts_endpoint = POSTS_ENDPOINT


class GetPostsAPI:

    def __init__(self,client):
        self.client = client

    def get_all_posts(self):
        response = self.client.get_request(posts_endpoint)
        return response

