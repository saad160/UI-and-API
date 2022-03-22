import json

import bcolors
import requests

# end point and auth_token
endpoint = "https://jsonplaceholder.typicode.com/users"  # End Point


# File Read
json_open = open('CreateUser.json', 'r')  # open json file
json_read = json_open.read()  # read json file
json_load = json.loads(json_read)  # load json file


jason_data = ['empty_json', 'valid_data']

for i in jason_data:
    json_dump = json.dumps(json_load[i])  # convert json to string
    json_split = json_dump.split()  # split the json so that we can access the status key
    json_status = json_split[1]  # index of status
    actual_result = json_status.replace(',', '')  # Replace extra space etv from status
    response = requests.post(endpoint, json_dump)  # Post Request
    print(bcolors.BOLD + "Response Body against " + i + " json body" + bcolors.END)
    print(json.dumps(response.json(), indent=4))  # Response
    status_code = str(response.status_code)  # status code
    print("Status Code")
    print(status_code)

    # Test Case Pass or Fail
    if status_code == actual_result:
        print('Test Case Status :' + bcolors.BLUEIC + ' Pass' + bcolors.END)
    else:
        print('Test Case Status :' + bcolors.FAIL + ' FAIL ' + bcolors.END)