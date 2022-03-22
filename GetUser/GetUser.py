import json
import requests


endpoint = "https://jsonplaceholder.typicode.com/users"  # End Point


response = requests.get(endpoint)  # get request for Bank Details
print(json.dumps(response.json(), indent=4))