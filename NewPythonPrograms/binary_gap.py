count=0
n=9
adjacent=[]
binary_value=bin(n)
value=binary_value[2:]
print(value)
line=len(value)
if value[0]=="1" and value[1:]=="0"*(line-1):
    count=0
    adjacent.append(count)
elif value[0]=="1" and value[1:]=="1"*(line-1):
    count=1
    adjacent.append(count)
else:
    for i in range(len(value)):
        for j in range(i+1,len(value)):
            if i%2==0 and j%2==0 and value[i]=="1" and value[j]=="1":
                count=count+1
                adjacent.append(count+1)
                count=0
            elif value[i]=="1" and value[i+1]=="1":
                count=count+1
                adjacent.append(count)
                count=0
if len(adjacent)==0:
    print(0)
else:
    print(max(adjacent))
