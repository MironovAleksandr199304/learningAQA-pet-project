import requests

class ClientAPI:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self,method, endpoint, json=None):
        url = f"{self.base_url}{endpoint}" ##self.base_url - self нужен потому что мы обращаемся к объекту внутри этого класса
        response = self.session.request(method=method,url=url,json=json) ##здесь self для session нужен чтобы указать, что мы обращаемся к session который инициализировали
        return response

    def get_request(self,endpoint):
        response = self._request("GET",endpoint=endpoint)
        return response

    def post_request(self,endpoint,payload):
        response = self._request("POST",endpoint=endpoint,json=payload)
        return response

    def put_request(self,endpoint,payload):
        response = self._request("PUT",endpoint=endpoint,json=payload)
        return response