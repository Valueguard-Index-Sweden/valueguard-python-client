

def handle_response(response):
    """ HandleResponse
    Function to check if the response is valid
    Throws exception if it is'nt
    """
    if (response.status_code != 200):
        raise Exception('Invalid response from server')
    return response.content.decode("utf-8")