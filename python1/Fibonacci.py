num=int(input("Enter the series"))
x=0
y=1
i=2
print(x, end=" ")
print(y, end=" ")
for i in range(i,num):
    z=x+y 
    print(z, end=" ")
    x=y
    y=z 
