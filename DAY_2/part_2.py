with open('input.txt') as file:
    txt = file.read()

lines = txt.split('\n')
data = [[int(a) for a in line.split(' ')] for line in lines]

def dampened(report: list[int]) -> list[list[int]]:
    reports = [report[:] for _ in range(len(report))]
    for i in range(len(reports)):
        reports[i].pop(i)

    reports.append(report[:])
    return reports

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
    safe = False
    for damp in dampened(report):
        if is_safe(damp):
            safe = True
    if safe:
        num += 1

print(num)

