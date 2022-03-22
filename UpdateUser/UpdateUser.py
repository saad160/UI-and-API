import json

import bcolors
import requests


# end point and auth_token
endpoint = "https://jsonplaceholder.typicode.com/users/"  # End Point
user_input = input("please enter user id : ")

json_file = open('UpdateUser.json', 'r')  # open json file
json_read_file = json_file.read()  # read json file
json_load = json.loads(json_read_file)

json_dump = json.dumps(json_load)
resp1 = requests.patch(endpoint + user_input, data={ "name" : "ahmad saad", "email" : "saadch985@gmail.com"})
print(json.dumps(resp1.json(), indent=4))
print(resp1.status_code)