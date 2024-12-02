def diff(pair):
    return abs(pair[0] - pair[1])

with open('input.txt') as file:
    in_txt = file.read()

lines = [a.replace('   ', ' ') for a in in_txt.split('\n')]

list1, list2 = [], []

for line in lines:
    txt1, txt2 = line.split(' ')
    list1.append(int(txt1))
    list2.append(int(txt2))

list1.sort()
list2.sort()

pairs = [(list1[i], list2[i]) for i in range(len(list1))]

distances = [diff(pair) for pair in pairs]

print(sum(distances))
