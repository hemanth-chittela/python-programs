flowerbed=[1,0,0,0,1]
n=2
count=0
Flag=False
for i in range(len(flowerbed)):
    if i%2==0 and flowerbed[i]==1:
        continue
    elif i%2!=0 and flowerbed[i]==0:
        continue
    elif (flowerbed[i]==1 and flowerbed[i-1]==1) or (flowerbed[i]==1 and flowerbed[i+1])==1:
        count=count-1
        Flag=False
    elif i%2==0 and flowerbed[i]==0:
        flowerbed[i]=1
        count=count+1
        Flag=True
for x in range(len(flowerbed)):
    if x%2==0 and flowerbed[x]==1:
        continue
    elif x%2!=0 and flowerbed[x]==1:
        count=count-1
if count>=n:
    Flag=True
else:
    Flag=False

if Flag:
    print("True")
else:
    print("False")
