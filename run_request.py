import requests
import json

access_point = "https://api.github.com"

response_text = requests.get(access_point + "/rate_limit").text

print(json.loads(response_text))

