array1=[10,22,3,4,1,6,7,8,5,33,4,99,100]
new_array=[]
k=3
for i in array1:
    j=str(i)
    j=len(j)
    if j==k:
        new_array.append(i)
for numbers in new_array:
    num=int(numbers)
    print(num,end=" ")