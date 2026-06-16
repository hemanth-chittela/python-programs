number=int(input("Enter the number: "))
Flag=True
if number<=1:
    print("Not a prime")
else:
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            Flag=False
            break
    if Flag:
        print("It is a prime")
    else:
        print("it is not a prime")

