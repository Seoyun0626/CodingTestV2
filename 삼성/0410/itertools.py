# 순열

arr = [1, 2, 3, 4]
visited = [0] * len(arr)

def permutation(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutation(n, new_arr + [arr[i]])
            visited[i] = 0
print("순열")
permutation(2, [])

# 중복 순열

arr = [1, 2, 3, 4]

def product(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

print("중복 순열")
product(2, [])



# 조합

arr = [1, 2, 3, 4]
def combination(n, new_arr, c):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combination(n, new_arr + [arr[i]], i + 1)

print("조합")
combination(2, [], 0)

# 중복 조합

arr = [1, 2, 3, 4]

def combinations_with_replacement(n, new_arr, c):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]], i)

print("중복 조합")
combinations_with_replacement(2, [], 0)
