count=0 
for i in range(5):
    for j in range(i+1):
        if count%2==0:
            print("0",end=" ")
            count=count+1
        else:
            print("1",end=" ")
            count=count+1
    print()
