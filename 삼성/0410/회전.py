# 회전
## 정사각형, 직사각형 모두 가능 / zip함수 활용
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr_90 = list(map(list, zip(*arr[::-1])))
arr_180 = [tmp[::-1] for tmp in arr[::-1]]
arr_270 = [tmp[::-1] for tmp in list(map(list, zip(*arr[::-1])))[::-1]]

def print_arr(arr):
    for cow in arr:
        print(cow)
    print()

print_arr(arr)
print_arr(arr_90)
print_arr(arr_180)
print_arr(arr_270)