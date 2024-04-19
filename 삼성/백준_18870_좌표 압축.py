import sys
input = sys.stdin.readline

n = int(input())
x_index = list(map(int, input().split()))
result = []
for i in range(len(x_index)):
    num = x_index[i]
    cnt = 0
    tmp = []
    for j in range(len(x_index)):
        if i == j:
            continue
        if num > x_index[j] and x_index[j] not in tmp:
            cnt += 1
            tmp.append(x_index[j])
    result.append(cnt)
print(*result)