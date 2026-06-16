list2=[22,243,423,2442,54,34,553,224,343,21,345,2245,243]
Found=False
target=int(input("Enter the value: "))
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        result=list2[i]+list2[j]
        if result==target:
            print(f"[{i,j}]")
            print(Found)
            Found=True
            print(Found)
            break
    if Found:
        break