list1=[2,3,4]
final=[]
Target=int(input("Enter the Target: "))
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==Target:
            final.append(i+1)
            final.append(j+1)
print(final)