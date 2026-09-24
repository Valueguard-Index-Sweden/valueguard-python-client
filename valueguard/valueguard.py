import requests
import json
import urllib.parse
from urllib.parse import quote


def _generate_request_search_criteria(search_criteria):
    """Build a query-string fragment from search criteria.

    Parameters
    ----------
    search_criteria : iterable
        Typically dict.items() containing key/value pairs.

    Returns
    -------
    str
        A string starting with '&' for each parameter, matching the old format.
    """
    url = ""
    for key, value in search_criteria:
        value = _change_array_to_string(value)
        url += f"&{quote(str(key))}={quote(str(value))}"
    return url

def _change_array_to_string(value):
    """Convert list values to a comma-separated string.

    This preserves the old behavior where list query parameters are sent as a
    single comma-separated value.
    """
    if isinstance(value, list):
        return ",".join(value)
    return value

class Client:
    # Default configuration
    server_url = "https://api-prod.valueguard.se"
    __oauth2_client_name = "api"
    _verify_ssl = True

    # Auth state
    access_token = ""
    refresh_token = ""

    def __init__(self):
        self.session = requests.Session()

    # -------------------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------------------

    def _decode_error(self, response):
        """Decode an error response safely."""
        return response.content.decode("utf-8", errors="replace")

    def _handle_json_response(self, response):
        """Return parsed JSON or raise an exception on non-200 responses."""
        if response.status_code != 200:
            raise Exception(self._decode_error(response))
        return response.json()

    def _handle_content_response(self, response):
        """Return raw response content or raise an exception on non-200 responses."""
        if response.status_code != 200:
            raise Exception(self._decode_error(response))
        return response.content

    def _build_url(self, path, search_criteria=None, include_access_token=True):
        """Build a full request URL.

        Parameters
        ----------
        path : str
            API path starting with '/'.
        search_criteria : dict | None
            Optional query criteria.
        include_access_token : bool
            Whether to append access_token in the query string.

        Returns
        -------
        str
            Fully formatted URL.
        """
        if search_criteria is None:
            search_criteria = {}

        if include_access_token:
            url = f"{self.server_url}{path}?access_token={quote(self.access_token)}"
        else:
            url = f"{self.server_url}{path}"

        url += _generate_request_search_criteria(search_criteria.items())
        return url

    def _get_json(self, path, search_criteria=None, include_access_token=True):
        """Perform a GET request and return JSON."""
        url = self._build_url(
            path=path,
            search_criteria=search_criteria,
            include_access_token=include_access_token,
        )
        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def _get_content(self, path, search_criteria=None, include_access_token=True):
        """Perform a GET request and return raw bytes."""
        url = self._build_url(
            path=path,
            search_criteria=search_criteria,
            include_access_token=include_access_token,
        )
        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_content_response(response)

    def _post_json_body(self, path, payload=None):
        """Perform a POST request with JSON body and return JSON."""
        if payload is None:
            payload = {}

        url = self._build_url(path=path, include_access_token=True)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = self.session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json=payload,
        )
        return self._handle_json_response(response)

    # -------------------------------------------------------------------------
    # Authentication
    # -------------------------------------------------------------------------

    def authenticate(self, username, password):
        """Authenticate with username and password.

        Retrieves both access token and refresh token.
        """
        url = (
            f"{self.server_url}/oauth/token"
            f"?client_id={self.__oauth2_client_name}"
            f"&grant_type=password"
            f"&username={quote(username)}"
            f"&password={quote(password)}"
        )

        response = self.session.post(url, verify=self._verify_ssl)

        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json["access_token"]
            self.refresh_token = response_json["refresh_token"]
        else:
            raise Exception(self._decode_error(response))

    def renew_access_token(self):
        """Renew the access token using the refresh token."""
        url = (
            f"{self.server_url}/oauth/token"
            f"?client_id=api"
            f"&grant_type=refresh_token"
            f"&refresh_token={quote(self.refresh_token)}"
        )

        response = self.session.post(url, verify=self._verify_ssl)

        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json["access_token"]
            self.refresh_token = response_json["refresh_token"]
        else:
            raise Exception(self._decode_error(response))

    # -------------------------------------------------------------------------
    # User
    # -------------------------------------------------------------------------

    def user(self):
        """Get the authenticated user."""
        return self._get_json("/v0/users/me")

    def user_roles(self):
        """Get roles for the authenticated user."""
        return self._get_json("/v0/users/me/roles")

    # -------------------------------------------------------------------------
    # Household
    # -------------------------------------------------------------------------

    def household(self, search_criteria=None):
        """Retrieve household data."""
        return self._get_json("/v1/household", search_criteria)

    def household_registration(self, search_criteria=None):
        """Retrieve household registration data."""
        return self._get_json("/v1/household/registration", search_criteria)

    # -------------------------------------------------------------------------
    # Residential registry
    # -------------------------------------------------------------------------

    def residential_registry(self, offset, limit, search_criteria=None):
        """Retrieve residential registry data."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/residential/registry"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def residential_registry_markups(self, offset, limit, search_criteria=None):
        """Retrieve residential registry markups."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/residential/registry/markups"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def residential_registry_valuations(self, offset, limit, search_criteria=None):
        """Retrieve residential registry valuations."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/residential/registry/valuations"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    # -------------------------------------------------------------------------
    # Taxation registry
    # -------------------------------------------------------------------------

    def taxation_registry_units(self, offset, limit, search_criteria=None):
        """Retrieve taxation unit registry data."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/taxation/registry/units"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def taxation_registry_buildings(self, offset, limit, search_criteria=None):
        """Retrieve taxation building registry data."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/taxation/registry/buildings"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def taxation_registry_lands(self, offset, limit, search_criteria=None):
        """Retrieve taxation land registry data."""
        if search_criteria is None:
            search_criteria = {}

        url = (
            f"{self.server_url}/v1/taxation/registry/lands"
            f"?access_token={quote(self.access_token)}"
            f"&offset={quote(str(offset))}"
            f"&limit={quote(str(limit))}"
        )
        url += _generate_request_search_criteria(search_criteria.items())

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    # -------------------------------------------------------------------------
    # Valuation / sales / ads
    # -------------------------------------------------------------------------

    def valuation(self, search_criteria=None):
        """Make a valuation query."""
        return self._get_json("/v1/valuation", search_criteria)

    def sales_reference(self, search_criteria=None):
        """Get sales references."""
        return self._post_json_body("/v1/sales/reference", search_criteria)

    def sales(self, search_criteria=None):
        """Get sales."""
        return self._get_json("/v1/sales", search_criteria)

    def ads(self, search_criteria=None):
        """Get ads."""
        return self._get_json("/v1/ads", search_criteria)

    def ads_pdf(self, search_criteria=None):
        """Get PDF snapshot of an ad."""
        return self._get_content("/v1/ads/pdf", search_criteria)

    # -------------------------------------------------------------------------
    # Index
    # -------------------------------------------------------------------------

    def index_definitions(self, search_criteria=None):
        """Get index definitions."""
        return self._get_json("/v1/index/definitions", search_criteria)

    def index_definitions_complete(self, search_criteria=None):
        """Get complete index definitions."""
        return self._get_json("/v1/index/definitions/complete", search_criteria)

    def index_normalized(self, search_criteria=None):
        """Get normalized index."""
        return self._get_json("/v1/index/normalized", search_criteria)

    def index_best(self, search_criteria=None):
        """Get best index."""
        return self._get_json("/v1/index/best", search_criteria)

    def index_recount(self, search_criteria=None):
        """Get recounted index value."""
        return self._get_json("/v1/index/recount", search_criteria)

    def index_publishing_calendar(self, search_criteria=None):
        """Get index publishing calendar.

        This endpoint is public and does not use access_token.
        """
        return self._get_json(
            "/v1/index/publishing/calendar",
            search_criteria=search_criteria,
            include_access_token=False,
        )

    def index_statistics(self, search_criteria=None, public=False):
        """Get index statistics.

        Parameters
        ----------
        public : bool
            If True, use the public endpoint without access token.
        """
        if public:
            url = f"{self.server_url}/v1/index/statistics/public?"
            if search_criteria is None:
                search_criteria = {}
            url += _generate_request_search_criteria(search_criteria.items())
            response = self.session.get(url, verify=self._verify_ssl)
            return self._handle_json_response(response)

        return self._get_json("/v1/index/statistics", search_criteria)

    def index_volume(self, search_criteria=None):
        """Get index area volume."""
        return self._get_json("/v1/index/volume", search_criteria)

    # -------------------------------------------------------------------------
    # Area
    # -------------------------------------------------------------------------

    def area(self, search_criteria=None):
        """Get areas."""
        return self._get_json("/v1/area", search_criteria)

    def area_category(self, search_criteria=None):
        """Get area categories."""
        return self._get_json("/v1/area/category", search_criteria)

    def area_information(self, search_criteria=None):
        """Get area information."""
        return self._get_json("/v1/area/information", search_criteria)

    def area_information_dates(self, search_criteria=None):
        """Get area information dates."""
        return self._get_json("/v1/area/information/dates", search_criteria)

    def area_information_field(self, search_criteria=None):
        """Get area information fields."""
        return self._get_json("/v1/area/information/field", search_criteria)

    def area_information_tag(self, search_criteria=None):
        """Get area information tags."""
        return self._get_json("/v1/area/information/tag", search_criteria)

    def area_polygon(self, search_criteria=None):
        """Get area polygons."""
        return self._get_json("/v1/area/polygon", search_criteria)

    # -------------------------------------------------------------------------
    # Market share / references
    # -------------------------------------------------------------------------

    def sales_market_share(self, search_criteria=None):
        """Get sales market share."""
        return self._post_json_body("/v1/sales/market-share", search_criteria)

    def ads_reference(self, search_criteria=None):
        """Get ads references."""
        return self._post_json_body("/v1/ads/reference", search_criteria)

    def ads_market_share(self, search_criteria=None):
        """Get ads market share."""
        return self._post_json_body("/v1/ads/market-share", search_criteria)

    # -------------------------------------------------------------------------
    # Housing association
    # -------------------------------------------------------------------------

    def housing_association(self, org_number):
        """Get information about a housing association."""
        url = (
            f"{self.server_url}/v1/housing-association/{quote(org_number)}"
            f"?access_token={quote(self.access_token)}"
        )

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def housing_association_report(self, housing_association_id, year):
        """Get the annual report PDF for a housing association."""
        url = (
            f"{self.server_url}/v1/housing-association/report"
            f"?housing_association_id={quote(str(housing_association_id))}"
            f"&year={quote(str(year))}"
            f"&access_token={quote(self.access_token)}"
        )

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_content_response(response)

    # -------------------------------------------------------------------------
    # Geocode
    # -------------------------------------------------------------------------

    def geocode(self, query, limit=5, match_type="address", exact_match=False):
        """Geocode an address or place."""
        url = (
            f"{self.server_url}/v1/geocode"
            f"?access_token={quote(self.access_token)}"
            f"&query={quote(query)}"
            f"&limit={quote(str(limit))}"
            f"&match_type={quote(match_type)}"
            f"&exact_match={quote(str(exact_match).lower())}"
        )

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    # -------------------------------------------------------------------------
    # Projects
    # -------------------------------------------------------------------------

    def projects_new(self):
        """Fetch default data required to create a new project."""
        return self._get_json("/v1/projects/new")

    def projects(self, limit=10):
        """Fetch projects for the authenticated user."""
        url = (
            f"{self.server_url}/v1/projects"
            f"?access_token={quote(self.access_token)}"
            f"&limit={quote(str(limit))}"
        )

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def project(self, project_id):
        """Fetch a specific project."""
        url = (
            f"{self.server_url}/v1/projects/{quote(str(project_id))}"
            f"?access_token={quote(self.access_token)}"
        )

        response = self.session.get(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def create_project(self, project_data):
        """Create a new project."""
        return self._post_json_body("/v1/projects", project_data)

    def delete_project(self, project_id):
        """Delete a project."""
        url = (
            f"{self.server_url}/v1/projects/{quote(str(project_id))}"
            f"?access_token={quote(self.access_token)}"
        )

        response = self.session.delete(url, verify=self._verify_ssl)
        return self._handle_json_response(response)

    def update_project_name(self, project_id, name):
        """Update a project's name."""
        url = (
            f"{self.server_url}/v1/projects/{quote(str(project_id))}/name"
            f"?access_token={quote(self.access_token)}"
        )

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = self.session.post(
            url,
            verify=self._verify_ssl,
            headers=headers,
            json={"name": name},
        )
        return self._handle_json_response(response)