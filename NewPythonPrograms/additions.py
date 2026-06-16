def addition(n):
    list2=[]
    if n%2==0:
        full=n//2
        result=list2.append(full)
        print(result)
        result=list2.append(list2[0])
        print(list2)
    else:
        half=n//2
        result=list2.append(half)
        result=list2.append(n-half)
        print(list2)
addition(7)
