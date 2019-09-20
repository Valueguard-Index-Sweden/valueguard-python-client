import requests
from valueguard_client.helper import handle_response

SERVER_URL = "https://dataservice.valueguard.se"


def bostadsregistret(token, parameters):
    """ Bostadsregistret
    Anropet liknar referensprisanropet men hämtar informationen från bostadsregistret, ett nära nog
    komplett register över alla bostäder i Sverige.
    """
    url = SERVER_URL + '/stdds/bostadsregistret/download?access_token=' + token

    return handle_response(requests.post(url, parameters))

