from itertools import combinations

n = int(input())
money = list(map(int, input().split()))
check_money = []
max_money = sum(money)
flag = 0

for i in range(1, n + 1):
    tmp_money = (list(combinations(money, i)))
    for tmp_combi_num in tmp_money:
        check_money.append(sum(tmp_combi_num))
check_money = set(check_money)

for i in range(1, max_money):
    if i not in check_money:
        print(i)
        flag = 1
        break
if flag == 0:
    print(max_money + 1)