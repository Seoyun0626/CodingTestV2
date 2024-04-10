arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for cow in arr:
    print(cow)

def gravity():
    global arr
    n = len(arr) # 행
    m = len(arr[0]) # 열

    for y in range(n - 1):
        for x in range(m):
            p = y
            while (p >= 0 and arr[p + 1][x] == 0 and arr[p][x] == 1):
                arr[p + 1][x], arr[p][x] = arr[p][x], arr[p + 1][x]
                p -=1

gravity()

print("중력")
for cow in arr:
    print(cow)
