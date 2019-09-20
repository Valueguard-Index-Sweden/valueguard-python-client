from requests import get, post
from urllib.parse import quote
from valueguard_client.helper import handle_response


def auth_service(username, password, data_user):
    """ AuthService
    Function to get token from the AuthService
    Used to authenticate to the Dataservice
    """
    url = 'https://analys.valueguard.se/authService/rest/authenticateDataUser?user=' + quote(username) + \
          '&password=' + quote(password) + '&dataUser=' + quote(data_user)
    # print(url)
    return handle_response(get(url))


def populus(username, password):
    """ Populus
    Function to get token from the Populus authentication system
    Used to authenticate to Stdds
    """
    url = 'https://dataservice.valueguard.se/stdds/api/login'
    data = '{"username":"' + username + '", "password":"' + password + '"}'
    # print(url)
    return handle_response(post(url, data))['access_token']


