import requests
from valueguard_client.helper import handle_response

SERVER_URL = "https://dataservice.valueguard.se"


def bostadsregistret(token, parameters):
    """ Bostadsregistret

    """
    url = 'https://dataservice.valueguard.se/stdds/bostadsregistret/download?access_token=' + token
    return handle_response(requests.post(url, parameters))

