# 회전
## zip활용해서 회전
### 정사각형, 직사각형 모두 가능
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr_90 = list(map(list, zip(*arr[::-1])))
arr_180 = [tmp[::-1] for tmp in arr[::-1]]
arr_270 = [tmp[::-1] for tmp in list(map(list, zip(*arr[::-1])))[::-1]]

# for cow in arr:
#     print(cow)
# print()
# for cow in arr_90:
#     print(cow)
# print()
# for cow in arr_180:
#     print(cow)
# print()
# for cow in arr_270:
#     print(cow)
분