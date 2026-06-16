list1=[1,2,3]
result=0
position=1
for i in range(-1,(-1*len(list1))-1,-1):
    val=list1[i]*position
    result=result+val
    position=position*10
result=result+1
arr=[]
for j in str(result):
    arr.append(int(j))
print(arr)