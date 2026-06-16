for number in range(2,1001):
    Flag=False
    for i in range(2,number//2+1):
        if number%i==0:
            Flag=True
    if Flag:
        print("it is not a prime",number)
    else:
        print("it is a prime",number)

