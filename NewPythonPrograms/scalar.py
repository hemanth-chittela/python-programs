n=5
print("*"*n)
j=3
for i in range(n,0,-1):
    print("*"+" "*(n-j)+"*")
    j=j+1
    print()
    if j==n+1:
        print("*")
        break