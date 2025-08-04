import requests
import pprint

params = {
    'q': 'html'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()

print(response.status_code)

pprint.pprint(response_json)