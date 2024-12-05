import re

with open('input.txt') as file:
    content = file.read()

statements = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content)
print(statements)
total = 0
started = True
for statement in statements:
    if statement == 'do()':
        started = True
    elif statement == 'don\'t()':
        started = False
    else:
        if started:
            a, b = [x for x in re.split('[^0-9]', statement) if x]
            print(a, b)
            int_a = int(a)
            int_b = int(b)
            total += (int_a * int_b)

print(total)
