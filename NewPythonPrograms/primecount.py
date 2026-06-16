count=0
n=int(input("Enter the n:"))
for number in range(2,n):
    Flag=True
    for j in range(2,number//2+1):
        if number%j==0:
            Flag=False
            break
    if Flag:
        count=count+1
print(count)
