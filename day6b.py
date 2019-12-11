import csv

data = []
with open('day6a.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[0].split(')'))

def inheritance_map(orbits):
    # Create dictionary mapping object to what it orbits around 
    return {i[1]: i[0] for i in orbits}

def find_path_of_inheritance(orbits, planet, path=[]):
    # Recursively search through to find the number of degrees of orbit an object has
    if orbits[planet] == 'COM':
        return path + ['COM']
    else:
        return find_path_of_inheritance(orbits, orbits[planet], path+[orbits[planet]])

def find_optimal_path(path1, path2):
    # Find first point in common between the paths
    # Then find the number of steps
    for i in path1:
        if i in path2:
            first_common = i
            break
    return path1.index(first_common) + path2.index(first_common)

path_you = find_path_of_inheritance(inheritance_map(data), 'YOU')
path_san = find_path_of_inheritance(inheritance_map(data), 'SAN')
print(find_optimal_path(path_you, path_san))