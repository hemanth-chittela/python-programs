name="abaaba"
final=[]
temp=0
counting_final=0
for i in range(len(name)):
    if name[temp:i+1]==name[temp:i+1][::-1]:
        if len(name[temp:i+1])==1:
            continue
        else:
            final.append(name[temp:i+1])
            temp=i+1

for x in range(len(final)):
    counting_final=counting_final+1
if counting_final>=3:
    for y in range(len(final)):
        print(final[y])
else:
    print("Impossible")