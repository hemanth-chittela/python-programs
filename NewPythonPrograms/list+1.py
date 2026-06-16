list2=[23,24,2346,343]
if len(list2)>1:
    for i in range(len(list2)):
        if len(list2)-1==i:
            list2.append(list2[i]+1)
    list2.remove(list2[-2])
    print(list2)
elif list2[0]==9:
    print(f"[0,1]")
else:
    print(f"[{list2[0]+1}]")

