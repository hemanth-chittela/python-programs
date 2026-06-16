n=3
counting=0
for i in range(n+1):
    counting=counting+1
    if counting==n:
        print(i+1)
        break
    elif counting+1==n:
        print(i+1)
        break
    else:
        counting=counting+2
        i=i+1

