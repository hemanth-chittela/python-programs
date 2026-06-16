string="thisisthebest"
list1=["t","h","i","s","e","b","s"]
count=0
for i in list1:
    for j in string:
        if i==j:
            count=count+1
    print("count of",i,"is",count)
    count=0