arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for cow in arr:
    print(cow)

def gravity():
    n = len(arr)
    m = len(arr[0])
    for y in range(n - 1):
        for x in range(m):
            p = y
            # 현재칸이 아래로 내려갈 수 있으면 윗줄도 한칸씩 내려가야 함
            while 0 <= p and arr[p][x] == 1 and arr[p + 1][x] == 0:
                arr[p][x], arr[p + 1][x] = arr[p + 1][x], arr[p][x]
                p -= 1
gravity()
print("변화")
for cow in arr:
    print(cow)