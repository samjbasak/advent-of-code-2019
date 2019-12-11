#number_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
#number_input[1] = 12
#number_input[2] = 2
number_input = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,78,40,225,1102,52,43,224,1001,224,-2236,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1,191,61,224,1001,224,-131,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,86,74,225,1102,14,76,225,1101,73,83,224,101,-156,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,43,82,225,2,196,13,224,101,-6162,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,161,51,224,101,-70,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,102,52,187,224,1001,224,-832,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1102,19,79,225,101,65,92,224,1001,224,-147,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,16,90,225,1102,45,44,225,1102,92,79,225,1002,65,34,224,101,-476,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,644,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,659,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

def update_value(place, value, number_input):
    number_input[place] = value
    return number_input

def do_command(number_input, command, parameter1=None, parameter2=None, result_position=None):
    if command == 99:
        return number_input, 4, False
    elif command == 1:
        updated_value = parameter1 + parameter2
        return update_value(result_position, updated_value, number_input), 4, True
    elif command == 2:
        updated_value = parameter1 * parameter2
        return update_value(result_position, updated_value, number_input), 4, True
    elif command == 3:
        return update_value(parameter1, 1, number_input), 2, True
    elif command == 3:
        print(number_input[parameter1])
        return number_input, 2, True
    else:
        return number_input, 1, True

print(do_command(number_input, 1, 225,6,6))

def parameter_or_immediate(value, value_type, number_input):
    if value_type == 0:
        return number_input[value]
    elif value_type == 1:
        return value

def split_code(code):
    code = str(code)
    while len(code) < 5:
        code = '0' + code
    parameter1 = code[2]
    parameter2 = code[1]
    parameter3 = code[0]
    opcode = code[3:]
    return int(parameter1), int(parameter2), int(parameter3), int(opcode)

def perform_complicated_code(number_input):
    playing = True
    command_position = 0
    while playing:
        parameter1, parameter2, parameter3, opcode = split_code(number_input[command_position])
        if command_position < len(number_input) + 3:
            parameter1 = parameter_or_immediate(number_input[command_position+1], parameter1, number_input)
            parameter2 = parameter_or_immediate(number_input[command_position+2], parameter2, number_input)
            result_position = number_input[command_position+3]
            print(parameter1, parameter2, parameter3, opcode)
            number_input, step, playing = do_command(
                number_input,
                command = opcode,
                parameter1=parameter1,
                parameter2=parameter2,
                result_position=result_position)
            print(number_input[0:20])
        else:
            playing = False
        command_position += step
        


#perform_complicated_code(number_input)


#print(complicated_code(1002))
    
    
    

def try_comb(noun, verb, number_input):
    playing = True
    i = 0
    number_input[1] = noun
    number_input[2] = verb
    while playing:
        number_input, playing = do_command(i, number_input)
        i += 4
    return number_input[0]


