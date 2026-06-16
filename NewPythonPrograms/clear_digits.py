s="thisjfds"
s=list(s)
for x in range(len(s)):
    for i in range(len(s)):
        if s[i].isdigit():
            s.pop(i)
            s.pop(i-1)
            break
        else:
            continue
s="".join(s)
print(s)