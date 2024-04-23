n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort() # [1, 2, 2, 3, 3]
# print(weight)
cnt = 0

for i in range(len(weight) - 1):
    j = i + 1
    while j != len(weight):
        if weight[j] != weight[i]:
            break
        else:
            j += 1
    cnt += (len(weight) - j)
print(cnt)


