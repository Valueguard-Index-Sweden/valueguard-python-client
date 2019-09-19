# valueguard-python-client


## BETA VERSION!! 
* Currently only used by Adrian fort testing and issue tracking 



### Get token 

#### AuthService token
```python
from valueguard_client import authentication

auth_service_username = "<USERNAME>"
auth_service_password = "<PASSWORD>"
auth_service_data_user = "python-client-lib"

auth_service_token = authentication.auth_service(auth_service_username, auth_service_password, auth_service_data_user)
```


#### Populus token
```python
from valueguard_client import authentication

populus_username = "<USERNAME>"
populus_password = "<PASSWORD>"

populus_token = authentication.populus(populus_username, populus_password)
```
