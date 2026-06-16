num=99999992
sum=0
for i in range(1,num+1):
    if num%i==0 and i<num:
        sum=sum+i
if sum==num:
    print("true")
else:
    print("false")
