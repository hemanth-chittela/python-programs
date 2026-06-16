k=0
p=5
for i in range(0,p+1):
    print(" "*(p-i)+k*"*")
    if k==p:
        break
    else:
        k=k+1
