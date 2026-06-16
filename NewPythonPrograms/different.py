colors=[1,8,3,8,3]
count=0
distance=[]
for i in range(len(colors)):
    for j in range(i+1,len(colors)):
        if colors[i]==colors[j]:
            continue
        elif colors[i]!=colors[j]:
            distance.append(j-i)
print(max(distance))