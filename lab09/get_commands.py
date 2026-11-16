import requests

# curl -G -d "q=Gardner,MA&format=json&limit=1" -H "User-Agent: MWCC-student1" https://nominatim.openstreetmap.org/search
def get_coords(city, state):
    request_url = 'https://nominatim.openstreetmap.org/search'
    request_headers = {'q': f'{city},{state}'
                       'User-Agent': 'MWCC-student1'
                       'limit': '1'}
    return requests.get(request_headers, headers=request_headers).json

get_coords('Gardner','MA')


#def get_noaa_endpoint(lat, lon):
#    url = f'https://api.weather.gov/points/{lat},{lon}'

#    headers = {
#        User-Agent:MWCC-student1
#        }


def get_noaa_forecast(url):
    pass
