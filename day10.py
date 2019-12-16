asteroid_input = ['.###.#...#.#.##.#.####..','.#....#####...#.######..','#.#.###.###.#.....#.####',
        '##.###..##..####.#.####.','###########.#######.##.#','##########.#########.##.',
        '.#.##.########.##...###.','###.#.##.#####.#.###.###','##.#####.##..###.#.##.#.',
        '.#.#.#####.####.#..#####','.###.#####.#..#..##.#.##','########.##.#...########',
        '.####..##..#.###.###.#.#','....######.##.#.######.#','###.####.######.#....###',
        '############.#.#.##.####','##...##..####.####.#..##','.###.#########.###..#.##',
        '#.##.#.#...##...#####..#','##.#..###############.##','##.###.#####.##.######..',
        '##.#####.#.#.##..#######','...#######.######...####','#....#.#.#.####.#.#.#.##']


# asteroid_input = ['......#.#.','#..#.#....','..#######.','.#.#.###..','.#..#.....',
#                    '..#....#.#','#..#....#.','.##.#..###','##...#..#.','.#....####']
area_size = (len(asteroid_input), len(asteroid_input[0]) + 1)


def produce_list_of_ratios(area_size, possible_ratios = []):
    for row in range(-area_size[0], area_size[0]):
        for column in range(-area_size[1], area_size[1]):
            possible_ratios.append((row, column))
    return possible_ratios


def check_for_prime(value_to_check, prime_numbers):
    for i in prime_numbers:
        if value_to_check % i == 0:
            return False
    return True

def list_of_primes(max_value, primes=[2]):
    for i in range(3,max_value):
        if check_for_prime(i, primes):
            primes.append(i)
    return primes

def reduce_coord(start_coord, reduced_coord=False):
    if not reduced_coord:
        reduced_coord = start_coord
    elif start_coord == (0,0):
        return (0,0)
    for prime in prime_numbers:
        if reduced_coord[0] % prime == 0 and reduced_coord[1] % prime == 0:
            return reduce_coord(start_coord, (int(reduced_coord[0]/prime), int(reduced_coord[1]/prime)))
    return reduced_coord

def make_dictionary_of_ratios(list_of_ratios):
    dict_of_ratios = {}
    for coord in list_of_ratios:
        dict_of_ratios[coord] = reduce_coord(coord)
    return dict_of_ratios

def find_coordinates(asteroid_input):
    coords = []
    for row_counter, row in enumerate(asteroid_input):
        for column_counter, column in enumerate(row):
            if column == '#':
                coords.append((row_counter, column_counter))
    return coords

def find_gradient(start_asteroid, target_asteroid, dict_of_ratios):
    row_diff = target_asteroid[0] - start_asteroid[0]
    col_diff = target_asteroid[1] - start_asteroid[1]
    return dict_of_ratios[(row_diff, col_diff)]

def find_asteroids_in_site(asteroid, asteroids, dict_of_ratios):
    gradients = set()
    asteroids = find_coordinates(asteroid_input)
    asteroids.remove(asteroid)
    for other_asteroid in asteroids:
        gradients.add(find_gradient(asteroid, other_asteroid, dict_of_ratios))
    return len(gradients)

possible_ratios = produce_list_of_ratios(area_size)
prime_numbers = list_of_primes(area_size[0])
dict_of_ratios = make_dictionary_of_ratios(possible_ratios)
asteroids = find_coordinates(asteroid_input)

highest_num = [0, (0,0)]
for i in asteroids:
    in_view = find_asteroids_in_site(i, asteroids, dict_of_ratios)
    if in_view > highest_num[0]:
        highest_num = [in_view, i]

print(highest_num)