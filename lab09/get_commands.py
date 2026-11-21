import requests

## curl -G -d "q=Gardner,MA&format=json&limit=1" -H "User-Agent: MWCC-student1" https://nominatim.openstreetmap.org/search
def get_coords(city, state):
    request_url = 'https://nominatim.openstreetmap.org/search'
    request_params = {'q': f'{city},{state}',
                       'limit': '1',
                       'format': 'json'}
    request_headers = {'User-Agent': 'MWCC-student1'}
    response = requests.get(request_url, params=request_params, headers=request_headers)
    data = response.json()[0]
    return data['lat'],data['lon']

# curl https://api.weather.gov/points/42.5763523,-71.9952737
def get_noaa_endpoint(lat, lon):
    url = f'https://api.weather.gov/points/{lat},{lon}'
    headers = {'User-Agent': 'MWCC-student1'}
    response = requests.get(url, headers=headers).json()
    forecast_url = response['properties']['forecast']
    return forecast_url
#stuff = get_noaa_endpoint('42.5763523','-71.9952737')
#print(stuff)

def get_noaa_forecast(url):
    response = requests.get(url).json()
    data = response
    return data['properties']['periods']
#print(get_noaa_forecast('https://api.weather.gov/gridpoints/BOX/38,105/forecast'))
