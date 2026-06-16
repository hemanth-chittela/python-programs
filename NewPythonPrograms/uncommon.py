s1="this is super runner"
s2="super"
newlist=s1+" "+s2
s=newlist.split(" ")
counting={}
final_list=[]
for i in s:
    if i in counting:
        counting[i]=counting[i]+1
    else:
        counting[i]=1
print(counting)
for i,j in counting.items():
    if j==1:
        final_list.append(i)
print(final_list)

