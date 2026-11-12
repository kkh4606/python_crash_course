import requests
import json

# Make an API call, and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

response = requests.get(url=url)
print(f"Status code: {response.status_code}")

# Explore the structure of the data
response_dict = response.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
