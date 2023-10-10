import requests
# Must be installed (usually)

import json
# Comes with Python

def get_ip_address():
    api_url = "http://icanhazip.com"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.text

def get_weather():
    # https://www.weather.gov/documentation/services-web-api
    api_url = "https://api.weather.gov/points/{},{}"
    
    # The coords for Ketcham Auditorium
    lat, long = 38.94639548663478, -92.33062455810867
    
    response = requests.get(api_url.format(lat, long))
    
    if response.status_code == 200:
        return response.json()

def get_joke():
    # https://icanhazdadjoke.com/api
    api_url = "https://icanhazdadjoke.com/"
    
    h = {
        "Accept": "application/json"
    }
    
    response = requests.get(api_url, headers = h)
    
    if response.status_code == 200:
        return response.json()

def search_mods(query):
    # https://docs.modrinth.com/api-spec
    api_url = "https://api.modrinth.com/v2/{}"
    endpoint = "search"
    
    facets = [["categories:fabric"], ["project_type:mod"]]
    
    # :eyes:
    p = {
        "facets": json.dumps(facets),
        "query": query
    }
    
    response = requests.get(api_url.format(endpoint), params = p)
    
    print(response.url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        print(response.json())
    else:
        print(response.status_code())

print(search_mods("enough items"))