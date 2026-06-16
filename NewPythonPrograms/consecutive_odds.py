array1=[1,3,2]
count=0
Flag=False
for i in array1:
    if i%2!=0:
        count=count+1
        if count==3:
            Flag=True
    else:
        count=0
print(Flag)
