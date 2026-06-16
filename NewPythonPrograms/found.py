Flag=False
numbers=[1,65,3,35,34,77,43,21,67,44,5,6,2,8,6,11,2,5,88,5,90,98]
to_locate=int(input("Enter the number to locate: "))
for i in range(len(numbers)):
    if numbers[i]==to_locate:
        Flag=True
        break
    else:
        Flag=False
if Flag:
    print("located on the index",i,"which is",numbers[i])
else:
    print("not found")
