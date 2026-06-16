list1=[1,2,3,4,5,6,7]
Flag=False
Target=int(input("Enter the Number: "))
for i in range(len(list1)-1):
    if list1[i]+list1[i+1]==Target:
        Flag=True
        break
if Flag:
    print(i,i+1)
else:
    print("the target does not match in the subsequent numbers")