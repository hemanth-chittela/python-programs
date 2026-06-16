name="java is good programming language"
name1=name.split()
x=-1
for i in range(len(name1)):
    for j in range(len(name1[i])):
        if j+1<=len(name1[i]):
            print(name1[i][x],end="")
            x=x-1
    x=-1
    print()
        