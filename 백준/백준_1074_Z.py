# # 0행0열 시작
#
# n, r, c = map(int, input().split())
# topNum = 0
# r_final = 0
# c_final = 0
# r_raw = r
# c_raw = c
#
# ## n == 1인 경우
# if n == 1:
#     result = 2 * r + c
# else:
#     ## n != 1인 경우
#     for i in range(n, 1, -1):
#         if r >= 2 ** (i - 1):
#             r_index = 2 ** (i - 1)
#         else:
#             r_index = 0
#         if c >= 2 ** (i - 1):
#             c_index = 2 ** (i - 1)
#         else:
#             c_index = 0
#         # print(r_index, c_index)
#         topNum += r_index * (2 ** i) + c_index * (2 ** (i - 1))
#         # print(topNum)
#         r = r - r_index
#         c = c - c_index
#         # print(r_final, c_final)
#     result = 2 * r + c + topNum
# print(result)

n, r, c = map(int, input().split())
answer = 0

while n != 0:
    n -= 1
    if r < 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 0
    elif r < 2 ** n and c >= 2 ** n:
        answer += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    elif r >= 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    else:
        answer += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)
print(answer)

