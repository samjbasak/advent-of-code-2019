import csv

data = []
with open('day6a.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[0])

def split_orbits(orbits):
    return [orbit.split(')') for orbit in orbits]

def inheritance_map(orbits):
    orbits = split_orbits(orbits)
    return {i[1]: i[0] for i in orbits}

def find_path_of_inheritance(orbits, planet, count=0):
    if orbits[planet] == 'COM':
        return count+1
    else:
        return find_path_of_inheritance(orbits, orbits[planet], count+1)


total = 0
for i in inheritance_map(data):
    total += find_path_of_inheritance(inheritance_map(data), i)

print(total)