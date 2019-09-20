from urllib.parse import quote
import json
from requests import get
from valueguard_client.helper import handle_response

server_url = "https://analys.valueguard.se"


def complete_property_data(token, search_bean):
    """ CompletePropertyData

    """
    url = server_url + "/dataService/rest/completePropertyData?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))


def home_information(token, street_address, zip, format):
    """ HomeInformation

    """
    url = server_url + "/dataService/rest/homeInformation?auth=" + str(token) + "&streetAddress=" + str(street_address) + "&zip=" + str(zip) + "&format=" + str(format)
    # print(url)
    return handle_response(get(url))


def assessment(token, search_bean):
    """ Assessment

    """
    url = server_url + "/dataService/rest/assessment?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))


def best_index(token, search_bean):
    """ BestIndex

    """
    url = server_url + "/dataService/rest/bestIndex?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))


def index_normalized(token, index_id, min_date, max_date, reference_date, reference_value):
    """ IndexNormalized

    """
    url = server_url + "/dataService/rest/indexNormalized?auth=" + str(token) + "&indexId=" + str(index_id) + "&minDate=" + str(min_date) + "&maxDate=" + str(min_date) + "&referenceDate=" + str(reference_date) + "&referenceValue=" + str(reference_value)
    # print(url)
    return handle_response(get(url))


def brf(token, search_bean):
    """ Brf

    """
    url = server_url + "/dataService/rest/brf?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))


def addresses_from_brf(token,search_bean):
    """ AddressesFromBrf

    """
    url = server_url + "/dataService/rest/addressesFromBrf?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))


def office(token, wgs84_lat, wgs84_lon):
    """ Office

    """
    url = server_url + "/dataService/rest/office?auth=" + str(token) + "&wgs84Lat=" + str(wgs84_lat) + \
          "&wgs84Lon=" + str(wgs84_lon)
    # print(url)
    return handle_response(get(url))


def area(token, lat, lon):
    """ Area

    """
    url = server_url + "/dataService/rest/area?auth=" + str(token) + "&lat=" + str(lat) + "&lon=" + str(lon)
    # print(url)
    return handle_response(get(url))


def area_statistics(token, area_id, house_type, rooms_list, area_intervals, min_build_year, max_build_year, min_nr_in_category):
    """ AreaStatistics

    """
    url = server_url + "/dataService/rest/area?reaStatistics?auth=" + token + "&areaId=" + area_id + "&houseType=" + house_type + "&roomsList=" + \
          rooms_list + "&areaIntervals=" + quote(area_intervals) + "&minBuildYear=" + min_build_year + "&maxBuildYear=" + max_build_year + \
          "&minNrInCategory=" + min_nr_in_category
    # print(url)
    return handle_response(get(url))


def ad_broker_statistics(token, search_bean):
    """ AdBrokerStatistics

    """
    url = server_url + "/dataService/rest/adBrokerStatistics?auth=" + token + "&sb=" + quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(get(url))
