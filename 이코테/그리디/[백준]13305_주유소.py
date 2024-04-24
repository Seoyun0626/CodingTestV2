n = int(input())
length = list(map(int, input().split())) # 2 3 1
price = list(map(int, input().split())) # 맨 마지막 원소 사용X, 5 2 4 1
i = 0
answer = 0

while i != len(length):
    move = length[i]
    money = price[i]
    j = i + 1
    while True:
        if money > price[j]:
            i = j
            answer += (move * money)
            break
        else:
            move += length[j]
            j += 1
        if j == len(length):
            answer += (move * money)
            i = j
            break
print(answer)

