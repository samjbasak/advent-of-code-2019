number_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
number_input[1] = 12
number_input[2] = 2

def update_value(place, value, number_input):
    number_input[place] = value
    return number_input

def do_command(command_position, number_input):
    command = number_input[command_position]
    if command == 99:
        return number_input, False
    elif number_input[command_position+1] < len(number_input) and number_input[command_position+2] < len(number_input) and number_input[command_position+3] < len(number_input):
        first_value = number_input[number_input[command_position+1]]
        second_value = number_input[number_input[command_position+2]]
        result_position = command_position+3
        if command == 1:
            updated_value = first_value + second_value
            return update_value(number_input[result_position], updated_value, number_input), True
        elif command == 2:
            updated_value = first_value * second_value
            return update_value(number_input[result_position], updated_value, number_input), True
        else:
            return number_input, True
    else:
        return number_input, True

def parameter_or_immediate(value, value_type, number_input):
    if value_type == '0':
        return 

def complicated_code():
    pass

def try_comb(noun, verb, number_input):
    playing = True
    i = 0
    number_input[1] = noun
    number_input[2] = verb
    while playing:
        number_input, playing = do_command(i, number_input)
        i += 4
    return number_input[0]

for i in range(100):
    for j in range(100):
        value = try_comb(i, j, number_input.copy())
        if value == 19690720:
            print(100 * i + j)
            break
