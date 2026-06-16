number=int(input("Enter the range: "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(number-2):
    a,b=b,a+b
    c=a+b
    print(c,end=" ")