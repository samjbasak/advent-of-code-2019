def consecutive_digits(number):
    string_num = str(number)
    for i in range(len(string_num) - 1):
        if string_num[i] == string_num[i+1]:
            return True
    return False

def max_two_same_digits(number):
    string_num = str(number)
    checker = 0
    for i in string_num:
        if string_num.count(i) == 2:
            return True
    return False

def increasing_digits(number):
    string_num = str(number)
    for i in range(len(string_num) - 1):
        if int(string_num[i]) > int(string_num[i+1]):
            return False
    return True


print(max_two_same_digits(112233))
print(increasing_digits(112233))

counter = 0
for i in range(353096,843213):
    if max_two_same_digits(i) and increasing_digits(i):
        counter += 1

print(counter)