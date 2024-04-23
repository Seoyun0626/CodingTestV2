n = int(input())
info = list(map(int, input().split()))
result = 0

info.sort(reverse=True) # 3 2 2 2 1

while True:
    num = info.pop(0)
    if len(info) < (num - 1):
        break
    else:
        result += 1
        for _ in range(num - 1):
            info.pop(0)
    if len(info) == 0:
        break
print(result)
