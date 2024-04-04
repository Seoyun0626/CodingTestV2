from collections import deque
import sys
input = sys.stdin.readline
# 1 = on 0 = off
n = int(input())
j = 0
switch = [-1] * (n + 1)
line = list(map(int, input().split()))
# print(line)
for i in range(1, n + 1):
    switch[i] = line[j]
    j += 1


def boy(index):
    plus = index
    while index < len(switch):
        switch[index] = 1 - switch[index]
        index = (index + plus)
    # print(switch)

def girl(index):
    i = 1
    switch[index] = 1 - switch[index]
    while True:
        if switch[index - i] == -1 or (index + i) >= len(switch):
            break
        elif switch[index - i] == switch[index + i]:
            switch[index - i] = 1 - switch[index - i]
            switch[index + i] = 1 - switch[index + i]
            i += 1
        else:
            break


m = int(input())
for _ in range(m):
    person, num = map(int, input().split())
    # print(person, num)
    if person == 1:
        # print("n, num, switch", n, num, switch)
        if n == num:
            switch[num] = 1 - switch[num]
        if n > num:
            boy(num)
        # print(switch)
    else:
        if n == num:
            switch[num] = 1 - switch[num]
        elif n > num:
            girl(num)
        # print(switch)

for i in range(1, n + 1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()
