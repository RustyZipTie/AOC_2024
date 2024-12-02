with open('input.txt') as file:
    txt = file.read()

lines = txt.split('\n')
data = [[int(a) for a in line.split(' ')] for line in lines]
print(data[:10])

def is_safe(report: list[int]) -> bool:
    inc, dec = (False,) * 2
    for i in range(len(report) - 1):
        a, b = report[i], report[i + 1]
        diff = a - b
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        elif diff < 0:
            inc = True
        elif diff > 0:
            dec = True

    return not (inc and dec)

num = 0
for report in data:
    if is_safe(report):
        num += 1

print(num)

