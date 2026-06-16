height=[1,8,6,2,5,4,8,3,7]
sorting=sorted(height)
highest=max(sorting)
for i in height:
    if i==highest:
        height.remove(i)
second_higest=max(height)
print(pow(second_higest,2))