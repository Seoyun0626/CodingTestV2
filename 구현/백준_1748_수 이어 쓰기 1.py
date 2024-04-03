import sys
input = sys.stdin.readline
n = int(input())
result = 0
# answer = ""
# for i in range(1, n + 1):
#     answer += str(i)
# print(answer)

for i in range(1,len(str(n)) + 1):
    if n // (10 ** i) == 0:
        tmp = n % (10 ** i) #15
        cnt = tmp - (10 ** (i - 1)) + 1
        result += (cnt * i)
        # print(result)
    else:
        cnt = (10 ** i) - (10 ** (i - 1))
        result += (cnt * i)
        # print(result)
print(result)



