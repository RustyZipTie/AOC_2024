with open("input.txt") as file:
    contents = file.read()

lines = contents.split("\n")

middles = []

occurences = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "A":
            middles.append((x, y))

for x, y in middles:
    try:
        if x < 1 or y < 1:
            raise IndexError
        
        ul = lines[y-1][x-1]
        ur = lines[y-1][x+1]
        ll = lines[y+1][x-1]
        lr = lines[y+1][x+1]
        if (((ul == "M" and lr == "S") or (ul == "S" and lr == "M")) and \
           ((ur == "M" and ll == "S") or (ur == "S" and ll == "M"))):
            occurences += 1
    except IndexError:
        pass
        

print(occurences)
