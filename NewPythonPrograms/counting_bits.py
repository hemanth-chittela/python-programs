final=[]
s=2
count=0
for i in range(s+1):
    to_binary=bin(i)
    from_positon=to_binary[2:]
    for j in from_positon:
        if j=="0" and i==0:
            continue
        elif j=="1":
            count=count+1
    final.append(count)
    count=0
print(final)
