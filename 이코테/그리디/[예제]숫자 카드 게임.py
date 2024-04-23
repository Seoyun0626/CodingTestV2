n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

min_num = 0
for tmp_list in num:
    tmp_list.sort()
    min_num = max(min_num, tmp_list[0])
print(min_num)