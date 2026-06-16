a="aaa"
b="aaa"
counting=0
if a==b:
    print(-1)
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            counting=counting+1
        else:
            continue
    print(counting)
