import requests
import argparse
import sys
from get_commands import get_coords, get_noaa_endpoint, get_noaa_forecast

#MWCC Latitude: 42.59529
#MWCC Longitude: -71.98517
#Relavent NOAA URL: https://api.weather.gov/points/42.5953,-71.9852
#NOAA Endpoint URL: https://api.weather.gov/gridpoints/BOX/39,106/forecast

#forecast = requests.get('https://api.weather.gov/gridpoints/BOX/39,106/forecast').json()
#periods = forecast['properties']['periods']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--location', action='store_true', required=True, help='Enter your city and state (Format: gardner MA)')
    args = parser.parse_args()

    get_coords(sys.argv[0])
    
    print(sys.argv[0])


if __name__ == '__main__':
    main()
