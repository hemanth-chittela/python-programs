import math
Number=int(input("Enter the number: "))
for i in range(2,Number):
    Flag=False
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            Flag=True
    if Flag:
        print("This is not prime",i)
    else:
        print("This is prime",i)