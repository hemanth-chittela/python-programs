#addition of rows and columns.
'''
list1=[[1,2,3],[4,5,6],[8,9,19],[11,12,3]]
row=[]
column1=[]
sum=0
for i in range(len(list1[0])):
    print(len(list1))
    for j in range(0,len(list1)):
        print(len(list1))
        sum=sum+list1[j][i] 
    row.append(sum)
    sum=0
print("Sum of columns",row)
'''
'''
for row in range(len(list1)):
    for column in range(len(list1)):
        sum=sum+list1[column][row]
    column1.append(sum)
    sum=0
print("Sum of column",column1)
'''
'''
list1=[[1,2,3],[4,5,6],[7,8,9]]
row=[]
column1=[]
sum=0
for j in range(len(list1)):
    for i in range(len(list1)):
        sum=sum+list1[j][i]
    row.append(sum)
    sum=0
print("Sum of row",row)
'''

list1=[[1,2,3,4],[4,5,6,7],[8,9,19,20],[12,3,1,23],[8,5,32,4]]
row=[]
column1=[]
sum1=0
for i in range(len(list1[0])):  
    #print(len(list1[0]))
    for j in range(len(list1)): 
    #    print(len(list1))
        sum1=sum1+list1[j][i]
    row.append(sum1)
    sum1=0
print("Sum of columns",row)