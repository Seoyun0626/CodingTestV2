n = int(input())
info = []
room = []
for _ in range(n):
    start, final = map(int, input().split())
    info.append((start, final))
# print(info)

for s,t in info:
    flag = 0
    if len(room) == 0:
        room.append([s, t])
    else:
        for tmp_room in room:
            final = tmp_room[-1]
            if final <= s:
                flag = 1
                tmp_room.append(t)
                break
        if flag == 0:
            room.append([s, t])
print(len(room))
