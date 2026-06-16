list1=[1,2,3,1]
Flag=False
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            Flag=True
            break
    if Flag:
        break
if Flag:
    print("TRue")
else:
    print("False")