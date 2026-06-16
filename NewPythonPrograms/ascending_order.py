#with this code I can do both ascending order and descending order 
list1=[-2,4,-6,2,53,13,0,3]
print("original List",list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print("Ascending Order",list1)
max_value=len(list1)
print("Max value is",list1[max_value-1])

for a in range(len(list1)):
    for b in range(a+1,len(list1)):
        if list1[a]<list1[b]:
            list1[a],list1[b]=list1[b],list1[a]
print("Descending Order",list1)

#this is bubble sort
for k in range(len(list1)-1,0,-1):
    for p in range(k):
        if list1[p]>list1[p+1]:
            list1[p],list1[p+1]=list1[p+1],list1[p]
print("new ascending",list1)