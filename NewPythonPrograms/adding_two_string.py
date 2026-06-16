list1=[2,3,4,5,5,2]
for i in range(len(list1)):
    Flag=False
    if list1[i]==list1[i+1]:
        Flag=True
        break
if Flag:
    print("True")
else:
    print("False")