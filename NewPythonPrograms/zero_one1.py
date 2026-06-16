for i in range(10):
    for j in range(i+1):
        if i%2==0 and j%2==0:
            print("0",end=" ")
        elif i%2==0 and j%2!=0:
            print("1",end=" ")
        elif i%2!=0 and j%2==0:
            print("1",end=" ")
        elif i%2!=0 and j%2!=0:
            print("0",end=" ")
        elif i%2!=0:
            print("1",end=" ")
    print()