import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_index = set(x)
sort_x_index = sorted(x_index)
result = []
dic = {}
for i in range(len(sort_x_index)):
    dic[sort_x_index[i]] = i
# print(dic)

for num in x:
    result.append(dic[num])
print(*result)
