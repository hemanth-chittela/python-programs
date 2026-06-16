count=0
jewels="z"
stones="ZZ"
for i in range(len(jewels)):
    for j in range(len(stones)):
        if jewels[i]==stones[j]:
            count=count+1
        else:
            continue
print(count)