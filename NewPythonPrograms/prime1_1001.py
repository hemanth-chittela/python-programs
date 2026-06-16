Numbers=int(input("Enter the number: "))
for number in range(2,Numbers):
    Flag=False
    for i in range (2,number//2+1):
        if number%i==0:
            Flag=True
    if Flag:
        print("it is a not a prime",number)
    else:
        print("it is a prime",number)
