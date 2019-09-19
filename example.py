from valueguard_client import authentication, stdds, dataservice
import json
import os

auth_service_username = os.environ['AUTH_SERVICE_USERNAME']
auth_service_password = os.environ['AUTH_SERVICE_PASSWORD']
auth_service_data_user = os.environ['AUTH_SERVICE_DATA_USER']

auth_service_token = authentication.auth_service(auth_service_username, auth_service_password, auth_service_data_user)
print("Authservice token:" + auth_service_token)

populus_username = os.environ['POPULUS_USERNAME']
populus_password = os.environ['POPULUS_PASSWORD']

populus_token = authentication.populus(populus_username, populus_password)
print("populus token:" + populus_token)

###
# BOSTADSREGISTRET
##

print("bostadsregistret")
bostadsregistret_data = stdds.bostadsregistret(populus_token,
                                                   {
                                                       "antalMax": 2,
                                                       "offset": 10
                                                   })
print(bostadsregistret_data)
# ISSUE NOT WORKING
#json.loads(bostadsregistret_data)

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

print (assessment_data)


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


index_normalized_data = dataservice.index_normalized(auth_service_token, best_index_data, "2012-08-16", "2013-10-16", "2012-12-24", 10000000)

print(index_normalized_data)

address_from_brf_data = dataservice.addresses_from_brf(auth_service_token,
                               {
                                   "brfOrgNr":"717600-3460"
                               })

print(address_from_brf_data)

brf_data = dataservice.brf(auth_service_token,
                {
                    "treetAddress": "Granitvägen",
                    "streetNumber": "13",
                    "streetLetter": "C",
                    "zip": "75243"
                })

print(brf_data)


office_data = dataservice.office(auth_service_token, 60.6728, 13.7126)

print(office_data)

area_data = dataservice.area(auth_service_token, 59.858577, 17.638861)
print(area_data)


dataservice.area_statistics(auth_service_token,62,"br", "notused", "15:45:75:110:300", 1111, 4444, 10)


#ad_broker_statistics_data = dataservice.ad_broker_statistics(auth_service_token,)
#print(ad_broker_statistics_data)