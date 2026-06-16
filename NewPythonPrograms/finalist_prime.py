Number=int(input("Enter the number: "))
Flag=False
for i in range(2,Number):
    if Number%i==0:
        Flag=True
if Flag:
    print("it is not a prime")
else:
    print("it is a prime")

