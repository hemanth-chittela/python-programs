Number=int(input("Enter the Number: "))
Flag=False
for i in range(1,10):
    if (i**i)+((i+1)**(i+1))==Number:
        Flag=True
if Flag: 
    print("True")
else:
    print("False")
