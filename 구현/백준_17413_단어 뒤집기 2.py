import sys
input = sys.stdin.readline
flag = 1
i = 0
s = input()
while flag:
    if s[i] == "<":
        tag_tmp = ""
        tag_tmp += "<"
        i += 1
        while s[i] != ">":
            tag_tmp += s[i]
            i += 1
        tag_tmp += ">"
        i += 1
        print(tag_tmp, end="")
        if i == len(s):
            break
    elif s[i] == " ":
        print(s[i], end="")
        i += 1
    else:
        tmp = ""
        tmp += s[i]
        i += 1
        while s[i] != " " and s[i] != "<" and s[i] != len(s):
            tmp += s[i]
            i += 1
            if i == len(s):
                tmp = tmp[::-1]
                print(tmp, end="")
                flag = 0
                break
        if flag:
            tmp = tmp[::-1]
            print(tmp, end="")
