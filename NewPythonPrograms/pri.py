for number in range(101):
    Flag=False
    if number<=1:
        Flag=True
    for i in range(2,number//2+1):
        if number%i==0:
            Flag=True
            break
    if Flag:
        print("no prime",number)
    else:
        print("prime",number)