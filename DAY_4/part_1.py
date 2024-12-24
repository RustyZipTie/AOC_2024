directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (1, -1),
    (1, 1),
    (-1, 1)
)

with open("input.txt") as file:
    contents = file.read()

lines = contents.split("\n")

word = "XMAS"

occurences = 0

starts = []

print(len(lines))
print(len(lines[0]))
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == word[0]:
            starts.append((x, y))

# iterate over possible starts
for x, y in starts:
    # iterate over possible directions
    for dx, dy in directions:
        temp_x, temp_y = x, y
        direction_valid = True
        # iterate over each letter
        for letter in word:
            try:
                if letter != lines[temp_y][temp_x]:
                    raise ValueError
                if temp_y < 0 or temp_x < 0:
                    raise IndexError
            except(IndexError, ValueError) as e:
                direction_valid = False
                break
            temp_y += dy
            temp_x += dx
        if direction_valid:
            # print(x, y, '|', dx, dy)
            occurences += 1

print(occurences)
