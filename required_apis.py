# Get coordinates from Position stack API for any city
# Push coordinates to Sunrise-Sunset API
import requests

def retrieve_coordinates():

    token = input("Enter token: ")
    print('''Must use one of the country codes below: 
Australia = AU / Canada = CA / Ireland = IE / United States = US
Sunrise-Sunset API only supports the above countries

Cool places to check out Alert, CA; Barrow, US; Anchorage, US

    ''')
    country_of_choice = input("Enter a country: ")
    city_of_choice = input("Enter a city: ")
    base_url = 'http://api.positionstack.com/v1/forward?'

    url = f"{base_url}access_key={token}&query={city_of_choice}&country={country_of_choice}"

    response = requests.get(url)
    information = response.json()

    location_coordinates = [information["data"][0]['latitude'],information["data"][0]['longitude']]

    return location_coordinates

coordinates = retrieve_coordinates()

def retrieve_day_light(date):
    base_url = 'https://api.sunrise-sunset.org/json?'
    url = f"{base_url}&lat={coordinates[0]}&lng={coordinates[1]}&date={date}"

    response = requests.get(url)
    answer = response.json()

    daylight = answer["results"]["day_length"]
    
    return daylight
