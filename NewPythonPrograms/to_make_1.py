n=10000
count=0
count1=0
count_list=[]
s=n
while n!=1:
    if n%2==0:
        n=n//2
        count=count+1
        if n==1:
            break
    else:
        n=n+1
        count=count+1
        continue
count_list.append(count)
while s!=1:
    if s%2==0:
        s=s//2
        count1=count1+1
        if s==1:
            break
    else:
        s=s-1
        count1=count1+1
        continue
count_list.append(count1)
print(min(count_list))