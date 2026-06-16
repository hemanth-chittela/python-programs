s="bb"
wordDict=["a","b","bbb","bbbb"]
repeat=""
Flag=False
for a in wordDict:
    if a in s:
        s=s.replace(a,"")
        repeat=repeat+a
        Flag=True
    elif repeat in a:
        Flag=True
    else:
        Flag=False
if Flag:
    print("True")
else:
    print("False")