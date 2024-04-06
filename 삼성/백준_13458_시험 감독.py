n = int(input())
person = list(map(int, input().split()))
firstboss, secondboss = map(int, input().split())
cnt1 = 0
# print(person)
## 총 감독관 먼저 계산
cnt1 += len(person)
for i in range(len(person)):
    person[i] -= firstboss

# print(person)

## 부 감독관 계산
for j in range(len(person)):
    if person[j] <= 0:
        continue
    if (person[j] % secondboss) == 0:
        cnt1 += (person[j] // secondboss)
    else:
        cnt1 += (person[j] // secondboss + 1)
print(cnt1)


