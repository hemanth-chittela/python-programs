haystack="leetcode"
needle="leeto"
Flag=False
length=len(needle)
print(length)
for i in range(len(haystack)):
    if needle in haystack:
        if needle[0:length] in haystack[i:length]:
            Flag=True
            break
        else:
            length=length+1

if Flag:
    print(i)
else:
    print(-1)
