#number of ways
list1=[1,2,3,4,5,6,7,8,9]
count=0
for i in range(len(list1)):
    for j in range(len(list1)):
        print(i,j)
        count=count+1
print("count is",count)