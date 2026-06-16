#This will find the index of the target in the list

list1=[22,43,25,75,26,3,-3,5]
Number=int(input("Enter the target: "))
Flag=False
for index,value in enumerate(list1):
    if Number==value:
        Flag=True
        break
if Flag: 
    print("The element is in the index",index)
else:
    print("The element is not in the list1")