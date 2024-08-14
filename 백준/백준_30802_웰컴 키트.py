# 티셔츠 한장 + 펜 한 자루
# 티셔츠 6종류 + T장 묶음 -> 남아도 가능
# 펜 1종류 + P자루 묶음 or 한 자루씩 주문 -> 정확해야 함

n = int(input())
numInfo = list(map(int, input().split()))
t, p = map(int, input().split())
t_result = 0

for num in numInfo:
    tmp_result = num % t
    if tmp_result == 0:
        t_result += (num // t)
    else:
        t_result += (num // t + 1)

p_result1 = n // p
p_result2 = n % p

print(t_result)
print(p_result1, p_result2)
