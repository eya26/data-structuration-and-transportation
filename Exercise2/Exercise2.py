class Person:
    def __init__(self, id, name, city, school):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

file_path = 'Exercise2/users.txt'
persons = []

with open(file_path, 'r') as file:
    for line in file:
        id = line[0:4].strip()
        name = line[4:29].strip()
        city = line[30:59].strip()
        school = line[60:90].strip()

        person = Person(id, name, city, school)
        persons.append(person)


for person in persons:
    print(f"ID: {person.id}, Name: {person.name}, City: {person.city}, school: {person.school}")
