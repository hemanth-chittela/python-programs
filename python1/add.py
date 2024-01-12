sum=0
x=int(input("Enter the number"))
while x>0:
    if(x>0):
        p=x%10
        sum=sum+p
        x=x//10
print(sum)
