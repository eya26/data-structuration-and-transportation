file_path = 'Exercise1/months.txt'
list = []

with open(file_path, 'r') as file:
    for line in file:
        list.append(line.strip())

print(list)

