import requests
from config.config import Config

class RequestBuilder:
    def __init__(self):
        self.base_url = Config.get_base_url()

    def build_get_request_url(self, endpoint):
        url = self.base_url + endpoint
        return url

    def send_request(self, url):
        
        response = requests.get(url)
        return response