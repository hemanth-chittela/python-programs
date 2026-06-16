list1=[1,2,3,4,4,4,4,5,6,7]
k=5
count=1
Flag=False
for i in range(len(list1)-1):
    if k>count:
        if list1[i]+1==list1[i+1]:
            count=count+1
            Flag=True
        else:
            Flag=False
            count=1
if k==count:
    Flag=True
else:
    Flag=False
if Flag:
    print("True")
else:
    print("False")