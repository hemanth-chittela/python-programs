numbers=[1,2,0]
flag=False
count1=0
count2=0
for i in range(len(numbers)-1):
    if numbers[i]<numbers[i+1]:
        count1=count1+1
        flag=True
    elif numbers[i]>numbers[i+1]:
        count2=count2+1
        flag=True
    elif numbers[i]==numbers[i+1]:
        flag=True
        count1=count1+1
        count2=count2+1

if count1==len(numbers)-1:
    flag=True
elif count2==len(numbers)-1:
    flag=True
else:
    flag=False

if flag:
    print("True")
else:
    print("False")