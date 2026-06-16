c=5
flag=False 
for i in range(1,10):
    if (i**i)+((i+1)*(i+1))==c:
        flag=True

if flag:
    print ("True")
else:
    print ("False")