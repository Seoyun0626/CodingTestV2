s = input()
i = 0
result = []
cnt = 0
j = 0
cnt2 = 0
while i != len(s):
    if "0" == s[i]:
        i += 1
    else:
        cnt += 1
        while "1" == s[i]:
            i += 1
            if i == len(s):
                break
result.append(cnt)

while j != len(s):
    if "1" == s[j]:
        j += 1
    else:
        cnt2 += 1
        while "0" == s[j]:
            j += 1
            if j == len(s):
                break

result.append(cnt2)
print(min(result))