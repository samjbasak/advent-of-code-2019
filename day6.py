import csv

data = []
with open('day6a.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[0].split(')'))

def inheritance_map(orbits):
    return {i[1]: i[0] for i in orbits}

def find_path_of_inheritance(orbits, planet, count=0):
    if orbits[planet] == 'COM':
        return count+1
    else:
        return find_path_of_inheritance(orbits, orbits[planet], count+1)

def calculate_total_inheritance(data):
    map_of_inheritance = inheritance_map(data)
    total = 0
    for i in map_of_inheritance:
        total += find_path_of_inheritance(map_of_inheritance, i)
    return total

print(calculate_total_inheritance(data))