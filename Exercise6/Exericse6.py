import json

class User:
    def __init__(self, id, name, city, school, age, is_teacher):
        self.id = id
        self.name = name
        self.city = city
        self.school = school
        self.age = age
        self.is_teacher = is_teacher


with open('Exercise6/users.json') as file:
    data = json.load(file)

users = []
for item in data:
    user = User(
        id=item['id'],
        name=item['name'],
        city=item['city'],
        school=item['school'],
        age=item['age'],
        is_teacher=item['is_teacher']
    )
    users.append(user)
  
for user in users:
    print("ID:", user.id)
    print("Name:", user.name)
    print("City:", user.city)
    print("School:", user.school)
    print("Age:", user.age)
    print("Is Teacher:", user.is_teacher)


