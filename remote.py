import json
import requests

url = "https://api.github.com/repos/stedolan/jq/commits?per_page=3"

r = requests.get(url)
r.status_code
