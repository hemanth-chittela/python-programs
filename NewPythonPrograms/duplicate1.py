string1="programming"
count=0
final=[]
for i in range(len(string1)):
    for j in range(len(string1)):
        if string1[i]==string1[j]:
            if string1[i] in final:
                continue
            else:
                final.append(string1[i])
final="".join(final)
print(final)
