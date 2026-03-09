import requests
import json
import urllib.parse


def _generate_request_search_criteria(search_criteria):
    url = ""
    for key, value in search_criteria:
        value = _change_array_to_string(value)
        url += "&" + urllib.parse.quote(key) + "=" + urllib.parse.quote(str(value))
    return url

def _change_array_to_string(value):
    """ Handles the check to see if the parameter is an array and then converts it to a string

    Parameters
    ----------
    :param value:
        The possible array or list we are going to convert to a string.

    Returns
    -------
    :return:
        A string. Either converted from an array or as it is.
    """
    if isinstance(value, list):
        parameters_string = ','.join(value)
        return parameters_string
    return value

class Client:
    # Static
    # server_url = "http://localhost:8080"
    server_url = "https://api.valueguard.se"
    __oauth2_client_name = "api"
    _verify_ssl=True

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
        response = requests.post(url, verify=self._verify_ssl)

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
        response = requests.post(url, verify=self._verify_ssl)
        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            #print(response_json)
        else:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))


    def user(self):
        """ Handles the query to get the user.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        url = self.server_url + "/v0/users/me?access_token=" + \
              urllib.parse.quote(self.access_token)
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
    
    def user_roles(self):
        """ Handles the query to get users roles.

        Returns
        -------
        :return:
            The query result in JSON format
        """
        url = self.server_url + "/v0/users/me/roles?access_token=" + \
              urllib.parse.quote(self.access_token)
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def household(self, search_criteria=None):
        """ Handles the query to retrieve data about a household.

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
        url = self.server_url + "/v1/household?access_token=" + \
              urllib.parse.quote(self.access_token) 
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
        
    def household_registration(self, search_criteria=None):
        """ Handles the query to retrieve data about a household registration.

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
        url = self.server_url + "/v1/household/registration?access_token=" + \
              urllib.parse.quote(self.access_token) 
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))    
        
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
        response = session.get(url, verify=self._verify_ssl)
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
        response = session.get(url, verify=self._verify_ssl)
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
        response = session.get(url, verify=self._verify_ssl)
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
        response = session.get(url, verify=self._verify_ssl)
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
         response = session.get(url, verify=self._verify_ssl)
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
          response = session.get(url, verify=self._verify_ssl)
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
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def sales_reference(self, search_criteria=None):
        """Handles the query to get sales references.

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

        session = requests.Session()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=search_criteria
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def sales(self, search_criteria=None):
        """ Handles the query to get sales.

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
        url = self.server_url + "/v1/sales?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def ads(self, search_criteria=None):
        """ Handles the query to get ads.

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
        url = self.server_url + "/v1/ads?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))    
    
    def ads_pdf(self, search_criteria=None):
        """ Handles the query to get pdf snapshot of ad.

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
        url = self.server_url + "/v1/ads/pdf?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return response.content  
    
    def index_definitions(self, search_criteria=None):
        """ Handles the query to get index definitions.

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
        url = self.server_url + "/v1/index/definitions?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
        
    def index_definitions_complete(self, search_criteria=None):
        """ Handles the query to get index definitions complete.

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
        url = self.server_url + "/v1/index/definitions/complete?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
    
    def index_normalized(self, search_criteria=None):
        """ Handles the query to get index normalized.

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
        url = self.server_url + "/v1/index/normalized?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def index_best(self, search_criteria=None):
        """ Handles the query to get best index.

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
        url = self.server_url + "/v1/index/best?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def index_recount(self, search_criteria=None):
        """ Handles the query to get an index recounted value.

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
        url = self.server_url + "/v1/index/recount?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def index_publishing_calendar(self, search_criteria=None):
        """ Handles the query to get the index publishing calendar.

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
        url = self.server_url + "/v1/index/publishing/calendar"
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
    
    def index_statistics(self, search_criteria=None, public=False):
        """ Handles the query to get the index publishing calendar.

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
            
        if public:
            url = self.server_url + "/v1/index/statistics/public?"
        else: 
            url = self.server_url + "/v1/index/statistics?access_token=" + \
                urllib.parse.quote(self.access_token)
            
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def index_volume(self, search_criteria=None):
        """ Handles the query to get the index area volume.

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
        url = self.server_url + "/v1/index/volume?access_token=" + \
              urllib.parse.quote(self.access_token)
        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area(self, search_criteria=None):
        """ Handles the query to get the areas.

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

        url = self.server_url + "/v1/area?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_category(self, search_criteria=None):
        """ Handles the query to get the area category.

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

        url = self.server_url + "/v1/area/category?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_information(self, search_criteria=None):
        """ Handles the query to get the area information.

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

        url = self.server_url + "/v1/area/information?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_information_dates(self, search_criteria=None):
        """ Handles the query to get the area information.

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

        url = self.server_url + "/v1/area/information/dates?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_information_field(self, search_criteria=None):
        """ Handles the query to get the area information fields.

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

        url = self.server_url + "/v1/area/information/field?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_information_tag(self, search_criteria=None):
        """ Handles the query to get the area information tags.

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

        url = self.server_url + "/v1/area/information/tag?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_polygon(self, search_criteria=None):
        """ Handles the query to get the area polygons.

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

        url = self.server_url + "/v1/area/polygon?access_token=" + \
                  urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def area_information_dates(self, search_criteria=None):
        """ Handles the query to get the area information dates.

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

        url = self.server_url + "/v1/area/information/dates?access_token=" + \
              urllib.parse.quote(self.access_token)

        url += _generate_request_search_criteria(search_criteria.items())
        # print(url)
        session = requests.Session()
        response = session.get(url, verify=self._verify_ssl)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))


    def sales_market_share(self, search_criteria=None):
        """ Handles the query to get the sales market share.

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

        url = self.server_url + "/v1/sales/market-share?access_token=" + \
              urllib.parse.quote(self.access_token)

        session = requests.Session()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=search_criteria
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def ads_reference(self, search_criteria=None):
        """Handles the query to get ads references.

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

        url = self.server_url + "/v1/ads/reference?access_token=" + \
              urllib.parse.quote(self.access_token)

        session = requests.Session()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=search_criteria
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def ads_market_share(self, search_criteria=None):
        """ Handles the query to get the ads market share.

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

        url = self.server_url + "/v1/ads/market-share?access_token=" + \
              urllib.parse.quote(self.access_token)

        session = requests.Session()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=search_criteria
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def housing_association(self, org_number):
        """Handles the query to get information about a housing association.

        Parameters
        ----------
        :param org-nr:
            Organization number used to filter the query.

        Returns
        -------
        :return:
            The query result in JSON format
        """


        url = (
                self.server_url
                + "/v1/housing-association/"
                + urllib.parse.quote(org_number)
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def housing_association_report(self, housing_association_id, year):
        """Handles the query to get the annual report for a housing association.

        Parameters
        ----------
        :param org-nr:
            Organization number used to filter the query.
        : param year
            Year for the report

        Returns
        -------
        :return:
            The PDF file content as bytes.
        """

        url = (
                self.server_url
                + "/v1/housing-association/report"
                + "?housing_association_id="
                + urllib.parse.quote(str(housing_association_id))
                + "&year="
                + urllib.parse.quote(str(year))
                + "&access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8", errors="replace"))

        return response.content

    def geocode(self, query, limit=5, match_type="address", exact_match=False):
        """Handles the query to geocode an address or place.

        Parameters
        ----------
        query : str
            The search string (e.g. street name, address).

        limit : int, optional
            Maximum number of results to return (default 5, max 10).

        match_type : str, optional
            Type of match to perform. Default is "address".

        exact_match : bool, optional
            Whether the match should be exact. Default False.

        Returns
        -------
        dict
            The API response returned as JSON containing geocode results.

        """

        url = (
                self.server_url
                + "/v1/geocode"
                + "?access_token="
                + urllib.parse.quote(self.access_token)
                + "&query="
                + urllib.parse.quote(query)
                + "&limit="
                + urllib.parse.quote(str(limit))
                + "&match_type="
                + urllib.parse.quote(match_type)
                + "&exact_match="
                + urllib.parse.quote(str(exact_match).lower())
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def projects_new(self):
        """Handles the query to fetch data required to create a new project.

        Returns
        -------
        dict
            The API response returned as JSON containing default project data.
        """

        url = (
                self.server_url
                + "/v1/projects/new"
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def projects(self, limit=10):
        """Handles the query to fetch projects for the authenticated user.

        Parameters
        ----------
        limit : int, optional
            Maximum number of projects to return.

        Returns
        -------
        dict
            The API response returned as JSON containing the projects.

        """

        url = (
                self.server_url
                + "/v1/projects"
                + "?access_token="
                + urllib.parse.quote(self.access_token)
                + "&limit="
                + urllib.parse.quote(str(limit))
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()


    def project(self, project_id):
        """Handles the query to fetch a specific project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.

        Returns
        -------
        dict
            The API response returned as JSON containing the project data.

        """

        url = (
                self.server_url
                + "/v1/projects/"
                + urllib.parse.quote(str(project_id))
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        response = session.get(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def create_project(self, project_data):
        """Handles the request to create a new project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing the full project configuration
            including search criteria and selected fields.

        Returns
        -------
        dict
            The API response returned as JSON containing the created project.

        """

        url = (
                self.server_url
                + "/v1/projects"
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=project_data
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def delete_project(self, project_id):
        """Handles the request to delete a project.

        Parameters
        ----------
        project_id : str
            The UUID of the project to delete.

        Returns
        -------
        dict
            The API response returned as JSON.

        """

        url = (
                self.server_url
                + "/v1/projects/"
                + urllib.parse.quote(str(project_id))
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        response = session.delete(
            url,
            verify=self._verify_ssl
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()

    def update_project_name(self, project_id, name):
        """Handles the request to update the name of a project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.

        name : str
            The new name for the project.

        Returns
        -------
        dict
            The API response returned as JSON.

        """

        url = (
                self.server_url
                + "/v1/projects/"
                + urllib.parse.quote(str(project_id))
                + "/name"
                + "?access_token="
                + urllib.parse.quote(self.access_token)
        )

        session = requests.Session()

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json={"name": name}
        )

        if response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

        return response.json()