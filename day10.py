asteroid_input = ['.###.#...#.#.##.#.####..','.#....#####...#.######..','#.#.###.###.#.....#.####',
        '##.###..##..####.#.####.','###########.#######.##.#','##########.#########.##.',
        '.#.##.########.##...###.','###.#.##.#####.#.###.###','##.#####.##..###.#.##.#.',
        '.#.#.#####.####.#..#####','.###.#####.#..#..##.#.##','########.##.#...########',
        '.####..##..#.###.###.#.#','....######.##.#.######.#','###.####.######.#....###',
        '############.#.#.##.####','##...##..####.####.#..##','.###.#########.###..#.##',
        '#.##.#.#...##...#####..#','##.#..###############.##','##.###.#####.##.######..',
        '##.#####.#.#.##..#######','...#######.######...####','#....#.#.#.####.#.#.#.##']

area_size = (len(asteroid_input), len(asteroid_input[0]))


def produce_list_of_ratios(area_size, possible_ratios = []):
    for row in range(area_size[0]):
        for column in range(area_size[1]):
            possible_ratios.append([row, column])
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

possible_ratios = produce_list_of_ratios(area_size)
prime_numbers = list_of_primes(area_size[0])

def reduce_list_of_ratios(possible_ratios, prime_numbers):
    new_ratios = []
    for row, column in possible_ratios:
        if non_reducable_numbers(row, column, prime_numbers):
            new_ratios.append([row, column])
    return new_ratios

def non_reducable_numbers(row, column, prime_numbers):

    if row in prime_numbers or column in prime_numbers:
        return True
    for prime in prime_numbers:
        if row % prime == 0 and column % prime == 0:
            return False
    return True

def reduce_coord(start_coord, reduced_coord=False):
    if not reduced_coord:
        reduced_coord = start_coord.copy()
    print(reduced_coord)
    for prime in prime_numbers:
        if reduced_coord[0] % prime == 0 and reduced_coord[1] % prime == 0:
            return reduce_coord(start_coord, [int(reduced_coord[0]/prime), int(reduced_coord[1]/prime)])
    return start_coord, reduce_coord

print(reduce_coord([10, 20]))

def find_coordinates(asteroid_input):
    coords = []
    for row_counter, row in enumerate(asteroid_input):
        for column_counter, column in enumerate(row):
            if column == '#':
                coords.append([row_counter, column_counter])
    return coords

def find_view_of_asteroid():
    pass

def find_asteroids_in_site(asteroid_input):
    pass


#print(reduce_list_of_ratios(possible_ratios, prime_numbers))
#print(len(find_coordinates(asteroid_input)))