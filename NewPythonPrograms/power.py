n=4194304
Flag=False
for i in range(12):
    if n==pow(4,i):
        Flag=True
        break
    else:
        Flag=False
if Flag:
    print("True")
else:
    print("False")
