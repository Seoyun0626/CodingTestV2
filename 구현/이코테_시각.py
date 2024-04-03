# 탐색 데이터가 100만개 이하일 때 완전 탐색 사용

n = int(input())
cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 05시 40분 13초 -> 054013에 3있는지 확인
            if "3" in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)