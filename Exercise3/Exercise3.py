class Person:
    def __init__(self, id, name, city, school):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

file_path = 'Exercise3/users.csv'
persons_list = []

with open(file_path, 'r') as file:
    header = file.readline()
    for line in file:
        attributes = line.strip().split(',')
        person = Person(attributes[0], attributes[1], attributes[2], attributes[3])
        persons_list.append(person)


for person in persons_list:
    print(f"ID: {person.id}, Name: {person.name}, City: {person.city}, School: {person.school}")
