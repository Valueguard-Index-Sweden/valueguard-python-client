import requests
import json
import urllib.parse


class Client:
    # Static
    # server_url = "http://10.10.2.222:31212"
    server_url = "http://localhost:8080"
    __oauth2_client_username = "api"

    # User settings;
    access_token = ""
    refresh_token = ""

    def __init__(self):
        pass

    # TODO url-encode username and password
    def authenticate(self, username, password):
        url = self.server_url + "/oauth/token?client_id=" + self.__oauth2_client_username + "&grant_type=password" \
                                                                                            "&username=" + username + \
              "&password=" + password
        # print(url)
        response = requests.post(url)
        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            # print(response_json)
        elif response.status_code != 200:
            # print(response.status_code)
            print(response.content.decode("utf-8"))
            raise Exception('Invalid response from server')

    def renew_access_token(self):
        url = self.server_url + "/oauth/token?client_id=api&grant_type=refresh_token&refresh_token=" + self.refresh_token
        print(url)
        response = requests.post(url)
        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            print(response_json)
        else:
            print(response.content.decode("utf-8"))

    def residential_registry(self, offset, limit):
        return self.residential_registry(offset, limit, {})

    def residential_registry(self, offset, limit, search_criteria):
        url = self.server_url + "/v1/residential/registry?access_token=" + self.access_token + "&offset=" + str(
            offset) + "&limit=" + str(limit)
        for key, value in search_criteria.items():
            url += "&" + urllib.parse.quote(key) + "=" + urllib.parse.quote(str(value))
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if (response.status_code != 200):
            print(response.content.decode("utf-8"))
            raise Exception('Invalid response from server')

        return json.loads(response.content.decode("utf-8"))
