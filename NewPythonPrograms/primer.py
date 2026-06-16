left=10
right=15
final=[]
count=0
prime_count=0
for i in range(left,right+1):
    s=bin(i)
    for x in range(len(s)):
        if s[x]=="1":
            count=count+1
        else:
            continue
    final.append(count)
    count=0
for number in range(len(final)):
    Flag=False
    if final[number]<=1:
        continue
    else:
        for j in range(2,final[number]//2+1):
            if final[number]%j==0:
                Flag=True
        if Flag:
            continue
        else:
            prime_count=prime_count+1
print(prime_count)