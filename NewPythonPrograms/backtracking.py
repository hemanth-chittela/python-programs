def backtracker(index,current,s):
    if index==len(s):
        print(current)
        return
    backtracker(index+1,current,s)
    backtracker(index+1,current+s[index],s)
s ="abc"
backtracker(0,"",s)
