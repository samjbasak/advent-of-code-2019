f = open('day8.txt', 'r')
content = [f.read()]

test_content = ['123456789012']

def split_string(list_of_layers, length_of_segment):
    if len(list_of_layers[-1]) <= length_of_segment:
        return list_of_layers
    else:
        list_of_layers = list_of_layers[:-1] + [list_of_layers[-1][:length_of_segment]] + [list_of_layers[-1][length_of_segment:]]
        return split_string(list_of_layers, length_of_segment)

def find_color(list_of_layers):
    color_layer = list(list_of_layers[0])
    for layer in list_of_layers[1:]:
        for counter, square in enumerate(layer):
            if color_layer[counter] == '2':
                color_layer[counter] = square
    return [''.join(color_layer)]

def build_string(list_of_layers, list_of_colors = []):
    if not list_of_layers:
        return list_of_colors
    else:
        new_string = ''
        for i in list_of_layers[0]:
            if i == '0':
                new_string += ' '
            else:
                new_string += '0'
        #print(new_string)
        list_of_layers.pop(0)
        list_of_colors.append(new_string)
        return build_string(list_of_layers, list_of_colors)

split = split_string(content, 25 * 6)
print(split)
colors = find_color(split)
print(colors)
list_of_layers = split_string(colors, 25)
print(list_of_layers)
colors = build_string(list_of_layers)

for i in colors:
    print(i)









'''
least_zeros = (10000, -1)
for counter, i in enumerate(split):
    if i.count('0') < least_zeros[0]:
        least_zeros = (i.count('0'), counter)

print(least_zeros)

print(split[least_zeros[1]].count('1'))
print(split[least_zeros[1]].count('2'))
print(split[least_zeros[1]].count('1') * split[least_zeros[1]].count('2'))
'''