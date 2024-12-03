import re

with open('input.txt') as file:
    content = file.read()

statements = re.findall("mul\([0-9]+,[0-9]+\)", content)

total = 0
for statement in statements:
    a, b = [x for x in re.split('[^0-9]', statement) if x]
    print(a, b)
    int_a = int(a)
    int_b = int(b)
    total += (int_a * int_b)

print(total)
