array1=[2,3,4,5,6,1,2,3,4]
for i in range(len(array1)-1,0,-1):
    for j in range(i):
        if array1[j]>array1[j+1]:
            array1[j],array1[j+1]=array1[j+1],array1[j]
print(array1)