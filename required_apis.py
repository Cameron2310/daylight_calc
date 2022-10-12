# Get coordinates from Position stack API for any city
# Push coordinates to Sunrise-Sunset API
import requests

# Class that creates necessary APIs
class my_APIs:
    def __init__(self, name, url, queries=None):
        self.name = name
        self.url = url
        self.queries = queries
    
    # Getters & Setters
    def get_queries(self):
        return self.queries
    
    def set_queries(self, queries):
        self.queries = queries

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url

# Child Class that creates request to Position Stack

class geo_APIs(my_APIs):
    def __init__(self, name, url, queries=None):
        super().__init__(name, url, queries)

    def retrieve_coordinates(self):

        token = input("Enter token: ")
        print('''Must use one of the country codes below: 
Australia = AU / Canada = CA / Ireland = IE / United States = US
Sunrise-Sunset API only supports the above countries

Cool places to check out Alert, CA; Barrow, US; Anchorage, US

        ''')
        country_of_choice = input("Enter a country: ")
        city_of_choice = input("Enter a city: ")

        self.set_queries({'token': token, 'city':city_of_choice, 'country': country_of_choice})


        query = self.get_queries()
        self.set_url(f"{self.get_url()}access_key={query['token']}&query={query['city']}&country={query['country']}")

        response = requests.get(self.get_url())
        information = response.json()

        location_coordinates = [information["data"][0]['latitude'],information["data"][0]['longitude']]

        return location_coordinates

# Child Class that creates request to Sunrise-Sunset API
class support_APIs(my_APIs):
    def __init__(self, name, url, queries=None):
        super().__init__(name, url, queries)
        self.queries = coordinates.retrieve_coordinates()

    def retrieve_day_light(self, date):
        query = self.get_queries()
        self.set_url(f"{self.get_url()}&lat={query[0]}&lng={query[1]}&date={date}")

        response = requests.get(self.get_url())
        answer = response.json()

        daylight = answer["results"]["day_length"]
        
        return daylight


coordinates = geo_APIs("Position Stack", 'http://api.positionstack.com/v1/forward?')
daylight_api = support_APIs("Sunrise Sunset", 'https://api.sunrise-sunset.org/json?')

