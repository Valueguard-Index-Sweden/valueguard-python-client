import requests
import json
import urllib.parse


def _generate_request_search_criteria(search_criteria):
    url = ""
    for key, value in search_criteria:
        url += "&" + urllib.parse.quote(key) + "=" + urllib.parse.quote(str(value))
    return url


class Client:
    # Static
    # server_url = "http://localhost:8080"
    server_url = "https://api.valueguard.se"
    __oauth2_client_name = "api"

    # User settings;
    access_token = ""
    refresh_token = ""

    def __init__(self):
        pass

    def authenticate(self, username, password):
        """ Uses user's credentials to authenticate.

        Generates the url to authenticate and request the access token as well
        as the refresh token from the server.

        Parameters
        ----------
        :param username:
            Username used to authenticate
        :param password:
            Password used to authenticates

        Raises
        ------
        :exception
            Exception raised when the server response is invalid
        """
        url = self.server_url + "/oauth/token?client_id=" + self.__oauth2_client_name + "&grant_type=password" \
                                                                                        "&username=" + \
              urllib.parse.quote(username) + \
              "&password=" + \
              urllib.parse.quote(password)
        # print(url)
        response = requests.post(url)

        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            # print(response_json)
        elif response.status_code != 200:
            # print(response.status_code)
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))

    def renew_access_token(self):
        """ Handles the renewal of the access token.

        """
        url = self.server_url + "/oauth/token?client_id=api&grant_type=refresh_token&refresh_token=" + \
              urllib.parse.quote(self.refresh_token)
        print(url)
        response = requests.post(url)
        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            print(response_json)
        else:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))

    def residential_registry(self, offset, limit, search_criteria=None):
        """ Handles the query to retrieve data from the residential registry.

        Uses offset and limit to break down the results of the query into chunks.

        Parameters
        ----------
        :param offset:
            The offset to start retrieving data from.
        :param limit:
            Defines the amount of data objects retrieved with each query.
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/residential/registry?access_token=" + \
              urllib.parse.quote(self.access_token) + \
              "&offset=" + urllib.parse.quote(str(offset)) + \
              "&limit=" + urllib.parse.quote(str(limit))
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def residential_registry_markups(self, offset, limit, search_criteria=None):
        """ Handles the query to retrieve data from the residential registry markups.

        Uses offset and limit to break down the results of the query into chunks.

        Parameters
        ----------
        :param offset:
            The offset to start retrieving data from.
        :param limit:
            Defines the amount of data objects retrieved with each query.
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/residential/registry/markups?access_token=" + \
              urllib.parse.quote(self.access_token) + \
              "&offset=" + urllib.parse.quote(str(offset)) + \
              "&limit=" + urllib.parse.quote(str(limit))
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def residential_registry_valuations(self, offset, limit, search_criteria=None):
        """ Handles the query to retrieve data from the residential registry valuations.

        Uses offset and limit to break down the results of the query into chunks.

        Parameters
        ----------
        :param offset:
            The offset to start retrieving data from.
        :param limit:
            Defines the amount of data objects retrieved with each query.
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/residential/registry/valuations?access_token=" + \
              urllib.parse.quote(self.access_token) + \
              "&offset=" + urllib.parse.quote(str(offset)) + \
              "&limit=" + urllib.parse.quote(str(limit))
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def taxation_registry_units(self, offset, limit, search_criteria=None):
        """ Handles the query to retrieve data from the taxation unit registry.

        Uses offset and limit to break down the results of the query into chunks.

        Parameters
        ----------
        :param offset:
            The offset to start retrieving data from.
        :param limit:
            Defines the amount of data objects retrieved with each query.
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/taxation/registry/units?access_token=" + \
              urllib.parse.quote(self.access_token) + \
              "&offset=" + urllib.parse.quote(str(offset)) + \
              "&limit=" + urllib.parse.quote(str(limit))
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def taxation_registry_buildings(self, offset, limit, search_criteria=None):
         """ Handles the query to retrieve data from the taxation building registry.

         Uses offset and limit to break down the results of the query into chunks.

         Parameters
         ----------
         :param offset:
             The offset to start retrieving data from.
         :param limit:
             Defines the amount of data objects retrieved with each query.
         :param search_criteria:
             Defines the search criteria used to filter the query.

         Returns
         -------
         :return:
             The query result in JSON format
         """
         if search_criteria is None:
             search_criteria = {}
         url = self.server_url + "/v1/taxation/registry/buildings?access_token=" + \
               urllib.parse.quote(self.access_token) + \
               "&offset=" + urllib.parse.quote(str(offset)) + \
               "&limit=" + urllib.parse.quote(str(limit))
         url += _generate_request_search_criteria(search_criteria.items())
         # print(url)
         session = requests.Session()
         response = session.get(url)
         if response.status_code != 200:
             # print(response.content.decode("utf-8"))
             raise Exception(response.content.decode("utf-8"))
         return json.loads(response.content.decode("utf-8"))

    def taxation_registry_lands(self, offset, limit, search_criteria=None):
          """ Handles the query to retrieve data from the taxation land registry.

          Uses offset and limit to break down the results of the query into chunks.

          Parameters
          ----------
          :param offset:
              The offset to start retrieving data from.
          :param limit:
              Defines the amount of data objects retrieved with each query.
          :param search_criteria:
              Defines the search criteria used to filter the query.

          Returns
          -------
          :return:
              The query result in JSON format
          """
          if search_criteria is None:
              search_criteria = {}
          url = self.server_url + "/v1/taxation/registry/lands?access_token=" + \
                urllib.parse.quote(self.access_token) + \
                "&offset=" + urllib.parse.quote(str(offset)) + \
                "&limit=" + urllib.parse.quote(str(limit))
          url += _generate_request_search_criteria(search_criteria.items())
          # print(url)
          session = requests.Session()
          response = session.get(url)
          if response.status_code != 200:
              # print(response.content.decode("utf-8"))
              raise Exception(response.content.decode("utf-8"))
          return json.loads(response.content.decode("utf-8"))

    def valuation(self, search_criteria=None):
        """ Handles the query to make valuations.

        Parameters
        ----------
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/valuation?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def sales_reference(self, search_criteria=None):
        """ Handles the query to get sales from reference.

        Parameters
        ----------
        :param search_criteria:
            Defines the search criteria used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        if search_criteria is None:
            search_criteria = {}
        url = self.server_url + "/v1/sales/reference?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
