#works for anysort of rows*columns
list1=[[1,22,3],[4,55,6,11,12,22,2,3,4],[7,88,9,1,2,],[2]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j]*2)