Number=int(input("Enter the Number: "))
for i in range(2**31):
    Flag=False
    if Number==i*i:
        Flag=True
        break
if Flag:
    print("True")
else:
    print("False")
