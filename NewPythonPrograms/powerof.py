Number=int(input("Enter the Number: "))
for i in range(31):
    Flag=False
    if Number==2**i:
        Flag=True
        break
if Flag:
    print("True")
else:
    print("False")
