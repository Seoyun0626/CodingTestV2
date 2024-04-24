from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = []
answer = 0
info = deque()
for _ in range(n):
    info.append(list(map(int, input().split())))

weight = []
for _ in range(k):
    weight.append(int(input()))
weight.sort()

info = deque(sorted(info))


for tmp_weight in weight:
    while info and info[0][0] <= tmp_weight:
        m, v = info.popleft()
        heapq.heappush(queue, -v)
    if queue:
        answer += (heapq.heappop(queue) * - 1)
print(answer)