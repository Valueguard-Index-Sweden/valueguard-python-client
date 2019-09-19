import requests
import urllib.parse
import json
import requests


def auth_service(username, password, data_user):
    url = 'https://analys.valueguard.se/authService/rest/authenticateDataUser?user=' + urllib.parse.quote(username) + \
          '&password=' + urllib.parse.quote(password) + '&dataUser=' + urllib.parse.quote(data_user)
    # print(url)
    response = requests.get(url)
    if (response.status_code != 200):
        raise Exception('Could not validate your Username / Password')
    return response.content.decode("utf-8")


def populus(username, password):
    url = 'https://dataservice.valueguard.se/stdds/api/login'
    data = '{"username":"' + username + '", "password":"' + password + '"}'
    # print(url)
    response = requests.post(url, data)
    if (response.status_code != 200):
        raise Exception('Could not validate your Username / Password')
    response_content = json.loads(response.content.decode("utf-8"))
    return response_content['access_token']
