import argparse
from get_commands import get_coords, get_noaa_endpoint, get_noaa_forecast

#MWCC Latitude: 42.59529
#MWCC Longitude: -71.98517
#Relavent NOAA URL: https://api.weather.gov/points/42.5953,-71.9852
#NOAA Endpoint URL: https://api.weather.gov/gridpoints/BOX/39,106/forecast

#forecast = requests.get('https://api.weather.gov/gridpoints/BOX/39,106/forecast').json()
#periods = forecast['properties']['periods']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--location', required=True, help='Enter your city and state (Format: "Gardner,MA")')
    parser.add_argument('-d', '--detailed', action='store_true', required=False, help='Detailed report')
    parser.add_argument('-w', '--week', action='store_true', required=False, help='Forecast of the week')
    parser.add_argument('-a', '--average', action='store_true', required=False, help='Average tempurature this week')
    args = parser.parse_args()

    if args.location:
        locate = args.location.split(',')
        coords = get_coords(locate[0],locate[1])
        endpoint = get_noaa_endpoint(coords[0],coords[1])
        periods = get_noaa_forecast(endpoint)

        if args.detailed:
            today = periods[0]
            print(f'It is currently: {today['detailedForecast']}')
        elif args.week:
            for day in range(len(periods)):
                print(f'{periods[day]['name']}: {periods[day]['shortForecast']}')
        elif args.average:
            all_temps = 0
            for day in range(len(periods)):
                all_temps += int(periods[day]['temperature'])
            average_temp = all_temps / len(periods)
            print(f'The average temperature this week is {average_temp} °{periods[0]['temperatureUnit']}')
        else:
            today = periods[0]
            print(f'Today is: {today['shortForecast']}')

if __name__ == '__main__':
    main()
