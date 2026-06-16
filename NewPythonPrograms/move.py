import random
list1=[]
for i in range(0,100):
    result=random.randint(0,1)
    list1.append(result)
for i in list1:
    if i==0:
        list1.append(i)
        list1.remove(i)
print(list1)