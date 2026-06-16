#sum of 2 consecutive numbers is equal to target
list1=[2,35,64,63,43,22,9,10]
print(list1)
Flag=False
Number=int(input("Enter the number: "))
for i in range(len(list1)-1):
    result=list1[i]+list1[i+1]
    if result==Number:
        print(f"[{i},{i+1}]")
        Flag=True
        break
if Flag:
    print("it works")
else:
    print("the target does not match the values in the index")
        
