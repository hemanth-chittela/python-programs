Number=2
list1={}
sum=0
Flag=False
to_string=str(Number)
while sum!=1:
    for i in to_string:
        sum=sum+int(i)**2
    if sum==1:
        Flag=True
        break
    else:
        to_string=str(sum)
        if sum in list1:
            list1[sum]=list1[sum]+1
            Flag=False
            break
        else:
            list1[sum]=1
            sum=0
            continue
if Flag:
    print("True")
else:
    print("False")
    