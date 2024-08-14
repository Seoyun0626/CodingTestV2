stringInfo = []
for _ in range(3):
    stringInfo.append(input())

for i in range(3):
    if stringInfo[i].isdecimal():
        num = int(stringInfo[i])
        num_index = i + 1
        break
resultNum = num + (4 - num_index)

if resultNum % 15 == 0:
    print("FizzBuzz")
elif resultNum % 3 == 0:
    print("Fizz")
elif resultNum % 5 == 0:
    print("Buzz")
else:
    print(resultNum)