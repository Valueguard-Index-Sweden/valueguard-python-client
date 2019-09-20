from valueguard_client import authentication, stdds, dataservice
import json
import os

auth_service_username = os.environ['AUTH_SERVICE_USERNAME']
auth_service_password = os.environ['AUTH_SERVICE_PASSWORD']
auth_service_data_user = os.environ['AUTH_SERVICE_DATA_USER']

# auth_service_token = authentication.auth_service(auth_service_username, auth_service_password, auth_service_data_user)
auth_service_token = authentication.auth_service(auth_service_username, auth_service_password)

print("Authservice token:" + auth_service_token)

populus_username = os.environ['POPULUS_USERNAME']
populus_password = os.environ['POPULUS_PASSWORD']

populus_token = authentication.populus(populus_username, populus_password)
print("populus token:" + populus_token)

###
# CompletePropertyData
##
''' EXAMPLE 1
complete_property_data = dataservice.complete_property_data(auth_service_token,
                                   {
                                       "category": "apartment",
                                       "floorAreaReference": 75,
                                       "floorReference": 3,
                                       "magic": 1,
                                       "monthlyFeeReference": 4000,
                                       "nrFloorsReference": -1,
                                       "nrRoomsReference": 2,
                                       "streetAddress": "Granitvägen",
                                       "streetNumber": 16,
                                       "streetLetter": "B",
                                       "zip": "75243",
                                       "wgs84Latitude": 59.84152420702172,
                                       "wgs84Longitude": 17.59763904880057,
                                       "squareSide": 1000
                                   })
print(complete_property_data)
'''
'''EXAMPLE 2
complete_property_data2 = dataservice.complete_property_data(auth_service_token,
                                                             {
                                                                 "buildYearReference": 1970,
                                                                 "buildYearWeight": 500,
                                                                 "category": "apartment",
                                                                 "contractDateWeight": 500,
                                                                 "contractDateReference": "2016-04-02T09:29:14.141Z",
                                                                 "distanceWeight": 500,
                                                                 "floorAreaReference": 75,
                                                                 "floorAreaWeight": 500,
                                                                 "floorReference": 3,
                                                                 "floorWeight": 500,
                                                                 "fromDate": "2004-12-06",
                                                                 "limit": 2000,
                                                                 "limitOnlyEstateagencyGroupData": False,
                                                                 "maxBuildYear": -1,
                                                                 "maxFee": -1,
                                                                 "maxFloor": -1,
                                                                 "maxNrFloors": -1,
                                                                 "maxPrice": -1,
                                                                 "maxRooms": -1,
                                                                 "maxSize": -1,
                                                                 "minBuildYear": -1,
                                                                 "minFee": -1,
                                                                 "minFloor": -1,
                                                                 "minNrFloors": -1,
                                                                 "minPrice": -1,
                                                                 "minRooms": -1,
                                                                 "minSize": -1,
                                                                 "monthlyCostReference": -1,
                                                                 "monthlyCostWeight": 0,
                                                                 "monthlyFeeReference": 4000,
                                                                 "monthlyFeeWeight": 500,
                                                                 "nrFloorsReference": -1,
                                                                 "nrFloorsWeight": 0,
                                                                 "nrRoomsReference": 2,
                                                                 "nrRoomsWeight": 500,
                                                                 "priceReference": -1,
                                                                 "priceWeight": 0,
                                                                 "propertyIds": [],
                                                                 "propertyIdsExcluded": [],
                                                                 "returnOnlyDisplayable": False,
                                                                 "rt90XCoordinate": 0,
                                                                 "rt90YCoordinate": 0,
                                                                 "squareSide": 450,
                                                                 "streetAddress": "",
                                                                 "streetNumber": -1,
                                                                 "toDate": "",
                                                                 "wgs84Latitude": 59.327472134716366,
                                                                 "wgs84Longitude": 18.04608760895923
                                                             })
print(complete_property_data2)
'''

'''EXAMPLE 3
complete_property_data3 = dataservice.complete_property_data(auth_service_token,
                                                             {
                                                                 "buildYearReference": 1970,
                                                                 "buildYearWeight": 0,
                                                                 "category": "house",
                                                                 "contractDateWeight": 500,
                                                                 "contractDateReference": "2012-03-02T13:47:41.424Z",
                                                                 "distanceWeight": 500,
                                                                 "floorAreaReference": 79,
                                                                 "floorAreaWeight": 500,
                                                                 "floorReference": 3,
                                                                 "floorWeight": 0,
                                                                 "fromDate": "2004-12-06",
                                                                 "limit": 2000,
                                                                 "limitOnlyEstateagencyGroupData": False,
                                                                 "maxFee": 12000,
                                                                 "maxSize": 300,
                                                                 "minBuildYear": 1920,
                                                                 "minFee": 0,
                                                                 "minFloor": 1,
                                                                 "minPrice": 0,
                                                                 "minRooms": 1,
                                                                 "minSize": 15,
                                                                 "monthlyCostReference": 0,
                                                                 "monthlyCostWeight": 0,
                                                                 "monthlyFeeReference": 4000,
                                                                 "monthlyFeeWeight": 0,
                                                                 "nrFloorsReference": 3,
                                                                 "nrFloorsWeight": 0,
                                                                 "nrRoomsReference": 3,
                                                                 "nrRoomsWeight": 500,
                                                                 "priceReference": 1000000,
                                                                 "priceWeight": 500,
                                                                 "returnOnlyDisplayable": False,
                                                                 "squareSide": 700000,
                                                                 "toDate": "2010-12-08",
                                                                 "wgs84Latitude": 56.87825401403527,
                                                                 "wgs84Longitude": 14.815636898486332
                                                             })
print(complete_property_data3)
'''

###
# BOSTADSREGISTRET
##

# EXAMPEL 1
'''
home_information1 = dataservice.home_information(auth_service_token,"Norra stationsgatan 99 lgh 1785", 11364, "AbeFormat")
print(home_information1)
'''

'''
# EXAMPEL 2 NOT WORKING
print("bostadsregistret")
bostadsregistret_data = stdds.bostadsregistret(populus_token,
                                               {
                                                   "antalMax": 2,
                                                   "offset": 10
                                               })
print(bostadsregistret_data)
# ISSUE NOT WORKING
# json.loads(bostadsregistret_data)
'''

###
# Assessment
##

'''
assessment_data = dataservice.assessment(auth_service_token,
                       {
                           "buildYearReference": "1944",
                           "category": "apartment",
                           "floorAreaReference": 38, 
                           "floorReference": 1.5,
                           "monthlyFeeReference": 2030,
                           "nrRoomsReference":1,
                           "rt90XCoordinate": 6565367,
                           "rt90YCoordinate": 1603648,
                           "sideAreaReference": 0,
                           "lotSizeReference":-1
                           })
print(assessment_data)
'''

###
# BestIndex
###

'''
best_index_data = dataservice.best_index(auth_service_token,
                       {
                           "buildYearReference": 1970,
                           "category": "apartment",
                           "floorAreaReference": 75,
                           "nrRoomsReference": 2,
                           "monthlyFeeReference": 4000,
                           "nrRoomsReference": 2,
                           "rt90XCoordinate": 0,
                           "rt90YCoordinate": 0,
                           "wgs84Latitude": 59.327472134716366,
                           "wgs84Longitude": 18.04608760895923,
                           "returnOnlyDisplayable": False,
                           "limitOnlyEstateagencyGroupData": False
                       })
print(best_index_data)
'''

###
# IndexNormalized
###
'''
index_normalized_data = dataservice.index_normalized(auth_service_token, "913011001800042", "2012-08-16", "2013-10-16", 
                                                     "2012-12-24", 10000000) 
print(index_normalized_data)
'''

###
# AddressFromBrf
###
'''
address_from_brf_data = dataservice.addresses_from_brf(auth_service_token,
                                                       {
                                                           "brfOrgNr": "717600-3460"
                                                       })
print(address_from_brf_data)
'''

###
# Brf
###
'''
brf_data = dataservice.brf(auth_service_token,
                {
                    "streetAddress": "Granitvägen",
                    "streetNumber": "13",
                    "streetLetter": "C",
                    "zip": "75243"
                })
print(brf_data)
'''

###
# Office
###
''' Not used / Not tested
office_data = dataservice.office(auth_service_token, 60.6728, 13.7126)

print(office_data)
'''

###
# Area
###
'''
# Example 1
area_data = dataservice.area(auth_service_token, 59.858577, 17.638861)
print(area_data)
'''

''' COULD'NT TEST!
# Example 2
area_statistics_1 = dataservice.area_statistics(auth_service_token, 62, "br", "notused", "15:45:75:110:300", 1111,
                                                4444, 10)
print(area_statistics_1)
'''

###
# AdBrokerStatistics
###
'''
ad_broker_statistics_data = dataservice.ad_broker_statistics(auth_service_token,
                                                             {
                                                                 "wgs84Latitude":59.346298255750256,
                                                                 "wgs84Longitude":18.05281162261963,
                                                                 "nrRoomsReference":"3",
                                                                 "floorAreaReference":"78",
                                                                 "lotSizeReference":"1500",
                                                                 "category":"apartment",
                                                                 "squareSide":"100"
                                                             })
print(ad_broker_statistics_data)
'''


“bostadsregistret”