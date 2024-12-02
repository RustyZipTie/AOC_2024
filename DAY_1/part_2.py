score = 0

with open('input.txt') as file:
    in_txt = file.read()

lines = [a.replace('   ', ' ') for a in in_txt.split('\n')]

list1, list2 = [], []

for line in lines:
    txt1, txt2 = line.split(' ')
    list1.append(int(txt1))
    list2.append(int(txt2))

for num in list1:
    score += num * list2.count(num)

print(score)
