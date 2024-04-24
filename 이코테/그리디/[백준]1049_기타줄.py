n, m = map(int, input().split())
one_price = []
total_price = []
answer = 0
for _ in range(m):
    total, one = map(int, input().split())
    total_price.append(total)
    one_price.append(one)

total_price.sort()
final_total = total_price[0]
one_price.sort()
final_one = one_price[0]

while n != 0:
    if n <= 6:
        if final_total <= n * final_one:
            answer += final_total
            break
        else:
            answer += (n * final_one)
            break
    else:
        if final_total <= 6 * final_one:
            answer += final_total
            n -= 6
        else:
            answer += (6 * final_one)
            n -= 6
print(answer)