list1=[10,20,20,30,40,50]
for i in list1[:]:
    if i==20:
        list1.remove(i)
print(list1)
