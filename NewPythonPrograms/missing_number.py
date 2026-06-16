items=[1,2,4,5,6]
for i in range(len(items)):
    if i in items:
        continue
    else:
        print(i)