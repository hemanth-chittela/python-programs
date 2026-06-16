s="Of all the gin joints in all the towns in all the world,   "
if len(s)==0:
    print(len(s))
else:
    count=0
    new=s.split(" ")
    for i in range(len(new)):
        if new[i]=="":
            continue
        else:
            count=count+1
    print(count)