def factorail(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorail(n-1)
x=factorail(5)
print(x)