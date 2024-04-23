import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
weight.sort() # [1, 1, 2, 3, 6, 7, 30]
target = 1 # target 미만은 계속 누적 합 -> 연산 가능한 범위
flag = 0

for x in weight:
    if target < x:
        flag = 1
        print(target)
        break
    target += x

if flag == 0:
    print(sum(weight) + 1)





