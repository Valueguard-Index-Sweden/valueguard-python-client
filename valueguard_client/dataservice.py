import urllib.parse
import json
import requests

server_url = "https://analys.valueguard.se"


def handle_response(response):
    if (response.status_code != 200):
        raise Exception('Invalid response from server')
    return response.content.decode("utf-8")


def complete_property_data(token, search_bean):
    url = server_url + "/dataService/rest/completePropertyData?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))


def home_information(token, street_address, zip, format):
    url = server_url + "/dataService/rest/homeInformation?auth=" + str(token) + "&streetAddress=" + str(street_address) + "&zip=" + str(zip) + "&format=" + str(format)
    # print(url)
    return handle_response(requests.get(url))


def assessment(token, search_bean):
    url = server_url + "/dataService/rest/assessment?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))


def best_index(token, search_bean):
    url = server_url + "/dataService/rest/bestIndex?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))


def index_normalized(token, index_id, min_date, max_date, reference_date, reference_value):
    url = server_url + "/dataService/rest/indexNormalized?auth=" + str(token) + "&indexId=" + str(index_id) + "&minDate=" + str(min_date) + "&maxDate=" + str(min_date) + "&referenceDate=" + str(reference_date) + "&referenceValue=" + str(reference_value)
    # print(url)
    return handle_response(requests.get(url))


def brf(token, search_bean):
    url = server_url + "/dataService/rest/brf?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))


def addresses_from_brf(token,search_bean):
    url = server_url + "/dataService/rest/addressesFromBrf?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))


def office(token, wgs84_lat, wgs84_lon):
    url = server_url + "/dataService/rest/office?auth=" + str(token) + "&wgs84Lat=" + str(wgs84_lat) + "&wgs84Lon=" + str(wgs84_lon)
    # print(url)
    return handle_response(requests.get(url))


def area(token, lat, lon):
    url = server_url + "/dataService/rest/area?auth=" + str(token) + "&lat=" + str(lat) + "&lon=" + str(lon)
    # print(url)
    return handle_response(requests.get(url))


def area_statistics(token, area_id, house_type, rooms_list, area_intervals, min_build_year, max_build_year, min_nr_in_category):
    url = server_url + "/dataService/rest/area?reaStatistics?auth=" + token + "&areaId=" + area_id + "&houseType=" + house_type + "&roomsList=" + \
          rooms_list + "&areaIntervals=" + urllib.parse.quote(area_intervals) + "&minBuildYear=" + min_build_year + "&maxBuildYear=" + max_build_year + \
          "&minNrInCategory=" + min_nr_in_category
    # print(url)
    return handle_response(requests.get(url))


def ad_broker_statistics(token, search_bean):
    url = server_url + "/dataService/rest/adBrokerStatistics?auth=" + token + "&sb=" + urllib.parse.quote(
        json.dumps(search_bean))
    # print(url)
    return handle_response(requests.get(url))
