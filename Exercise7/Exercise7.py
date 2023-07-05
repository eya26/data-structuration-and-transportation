import json

class City:
    def __init__(self,city, lat, lng, country, iso2, admin_name, capital, population, population_proper):
        self.city = city
        self.lat = lat
        self.lng = lng
        self.country = country
        self.iso2 = iso2
        self.admin_name = admin_name
        self.capital = capital
        self.population = population
        self.population_proper = population_proper

with open('Exercise7/french-cities.json') as file:
    data = json.load(file)

cities = []
for city in data:
    c = City(
        id=city['id'],
        name=city['name'],
        city=city['city'],
        school=city['school'],
        age=city['age'],
        is_teacher=city['is_teacher']
    )
    cities.append(c)