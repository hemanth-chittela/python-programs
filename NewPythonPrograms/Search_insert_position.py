list1=[1,3,5,6]
Target=int(input("Enter the target: "))
Flag=False
for i in range(len(list1)):
    if list1[i]==Target:
        Flag=True
        break
if Flag:
    print(i)
else:
    list1.append(Target)
    list1.sort()
    index=list1.index(Target)
    print(index)


