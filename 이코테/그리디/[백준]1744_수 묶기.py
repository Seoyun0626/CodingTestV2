import sys
input = sys.stdin. readline

n = int(input())
positive_num = []
negative_num = []
answer = 0
i = 0
j = 0
for _ in range(n):
    num = int(input())
    if num <= 0:
        negative_num.append(num)
    else:
        positive_num.append(num)

negative_num.sort()
positive_num.sort(reverse = True)


while i < len(negative_num):
    if (i + 1) != len(negative_num):
        answer += (negative_num[i] * negative_num[i + 1])
        i += 2
    else:
        answer += negative_num[i]
        break
while j < len(positive_num):
    if (j + 1) != len(positive_num):
        if positive_num[j + 1] == 1:
            answer += positive_num[j]
            j += 1
        else:
            answer += (positive_num[j] * positive_num[j + 1])
            j += 2
    else:
        answer += positive_num[j]
        break
print(answer)






