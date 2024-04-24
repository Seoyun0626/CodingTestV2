import sys
import heapq

input = sys.stdin.readline
n = int(input())
info = []
room = []
for _ in range(n):
    start, final = map(int, input().split())
    info.append((start, final))
info.sort() # 시작 시간 기준 정렬
# print(info)

heapq.heappush(room, info[0][1])

for i in range(1, len(info)):
    s, t = info[i][0], info[i][1]
    # room은 heapq구현 -> room[0] 항상 최솟값
    if room[0] <= s:
        heapq.heappop(room)
        heapq.heappush(room, t)
    else:
        heapq.heappush(room, t)
print(len(room))
