import requests
import json

class Client:
    server_url="http://localhost:8080";

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_server_url(self, url):
        self.server_url=url;

    def bostadsregistret(self, page_nr, page_size):
        url = self.server_url + "/api/v1/bostadsregistret/stream?pageNr=" + str(page_nr) + "&pageSize=" + str(page_size)
        #print(url)
        session = requests.Session()
        session.auth = (self.username, self.password)
        response = session.get(url)
        if (response.status_code != 200):
            raise Exception('Invalid response from server')
        return json.loads(response.content.decode("utf-8"))
