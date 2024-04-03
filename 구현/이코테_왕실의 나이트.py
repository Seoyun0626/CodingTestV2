x, y = 1, 1
move =[[-2, -1], [-2, 1], [2, -1], [2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2]]

count = 0
for dy, dx in move:
    if 1 <= x + dx < 6 and 1 <= y + dy < 6:
        count += 1
        x = x + dx
        y = y + dy
print(count)