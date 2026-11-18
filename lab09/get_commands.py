import requests

## curl -G -d "q=Gardner,MA&format=json&limit=1" -H "User-Agent: MWCC-student1" https://nominatim.openstreetmap.org/search
#def get_coords(city, state):
#    request_url = 'https://nominatim.openstreetmap.org/search'
#    request_headers = {'q': f'{city},{state}'}
#    request_params = {'User-Agent': 'MWCC-student1',
#                      'limit': '1'}
#    return requests.get(request_url, headers=request_headers, params=request_params).json
#
#print(get_coords('Gardner','MA'))

# curl https://api.weather.gov/points/42.5763523,-71.9952737
def get_noaa_endpoint(lat, lon):
    url = f'https://api.weather.gov/points/{lat},{lon}'
    headers = {'User-Agent': 'MWCC-student1',
               'limit': '1'}
    global response #Desperate attempt to make it work
    response = requests.get(url, headers=headers).json
    return response

get_noaa_endpoint('42.5763523','-71.9952737')
print(response)

def get_noaa_forecast(url):
    pass
