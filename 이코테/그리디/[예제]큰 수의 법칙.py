# 연속해서 같은 수 더할 때 K번 초과하지않고 M번 더해서 큰 수 만들기

# 5 8 3
# 2 4 5 4 6
# ==> 46

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
result = 0

num.sort(reverse=True)
first_num = num[0]
second_num = num[1]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_num
        m -= 1

    if m == 0:
        break

    if first_num == second_num:
        for j in range(k):
            if m == 0:
                break
            result += second_num
            m -= 1
    else:
        result += second_num
        m -= 1
print(result)





