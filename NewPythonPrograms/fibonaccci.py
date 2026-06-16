Number=int(input("Enter the range: "))
j=0
k=1
print(j,end=" ")
print(k,end=" ")
for i in range(2,Number):
    sum=j+k
    #print(sum,end=" ")
    j=k
    k=sum
    print(sum,end=" ")

0 1 1 2