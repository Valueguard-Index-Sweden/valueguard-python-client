import urllib.parse
import json
import requests

SERVER_URL="https://dataservice.valueguard.se"

def bostadsregistret(token, parameters):
    url = 'https://dataservice.valueguard.se/stdds/bostadsregistret/download?access_token=' + token
    response = requests.post(url, parameters)
    if (response.status_code != 200):
        raise Exception('Invalid response from server')
    return response.content.decode("utf-8")
