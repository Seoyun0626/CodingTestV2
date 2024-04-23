s = input()
result = 0

if len(s) >= 2:
    if s[0] == "0" or s[1] == "1" or s[0] == "1" or s[1] == "0":
        result = (int(s[0]) + int(s[1]))
    else:
        result = int(s[0]) * int(s[1])

    for i in range(2, len(s)):
        if int(s[i]) == 0 or int(s[i]) == 1 or result == 0 or result == 1:
            result += int(s[i])
        else:
            result *= int(s[i])
    print(result)
elif len(s) == 1:
    print(int(s[0]))

