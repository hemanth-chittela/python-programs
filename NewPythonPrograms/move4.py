list1=[1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0]
count=0
for i in list1:
    if i==0:
        count=count+1
list1=[x for x in list1 if x!=0]+[0]*count
print(list1)