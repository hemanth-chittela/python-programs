n=3
count=-1
count1=-1
answer=[]
for i in range(n+1):
    count1=count1+1
    for j in range(i+1):
        count=count+1
        if count!=n:
            continue
        else:
            answer.append(count1)
print(answer[0])