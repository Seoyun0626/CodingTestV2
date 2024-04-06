# 순열
arr = [1, 2, 3, 4]
visited = [0] * len(arr) # 순서 고려 -> 유일 visited배열 존재

def permutations(n, new_arr):
    global arr
    # 순서상관 O, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0
permutations(2, [])

# 중복 순열
arr = [1, 2, 3, 4]
def product(n, new_arr):
    global arr
    # 순서 상관 O, 중복 O
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])
product(2, [])

# 조합
## 현재 인덱스 +1 만큼을 매개변수로 계속 념겨주어야함
## 순서가 상관없고 중복 불가이기 때문에 현재 인덱스보다 가거나 작은 인텍스는 확인할 필요X
arr = [1, 2, 3, 4]
def combinations(n, new_arr, c):
    # 순서 상관X, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)
combinations(2, [], 0)

# 중복 조합
## 인덱스 의미하는 매개변수 추가 But 중복 가능 -> +1이 아닌 현재 인덱스 넘기기
arr = [1, 2, 3, 4]
def combinations_with_replacemen(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacemen(n, new_arr + [arr[i]], i)

combinations_with_replacemen(2, [], 0)