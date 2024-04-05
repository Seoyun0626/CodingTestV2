from itertools import combinations
from copy import deepcopy
n, m  = map(int, input().split())
graph = []
house = []
store = []
not_store = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            house.append((x, y))
for y in range(n):
    for x in range(n):
        if graph[y][x] == 2:
            store.append((x, y))
final_store = list(combinations(store, m))
# print(final_store)
# print(house)
def distance(chicken_store):
    tmp_result = 0
    # print(chicken_store)
    for home in house:
        tmp_distance = []
        x1, y1 = home[0], home[1]
        for chicken in chicken_store:
            x2, y2 = chicken[0], chicken[1]
            tmp_distance.append(abs(x1 - x2) + abs(y1 - y2))
        tmp_result += min(tmp_distance)
    return tmp_result


for tmp in final_store:
    chicken_distance = distance(tmp)
    result.append(chicken_distance)
print(min(result))

