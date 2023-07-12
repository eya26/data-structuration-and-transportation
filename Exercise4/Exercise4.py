import csv

class Person:
    def __init__(self, id, name, city, school):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

file_path = 'Exercise4/users.csv'
instances_list = []

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id, name, city, school = row
        instance = Person(id, name, city, school)
        instances_list.append(instance)
for instance in instances_list:
    print(f"ID: {instance.id}, Name: {instance.name}, City: {instance.city}, School: {instance.school}")
