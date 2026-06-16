string1="programming"
final={}
answer=[]
for i in range(len(string1)):
    if string1[i] in final:
        final[string1[i]]=final[string1[i]]+1
    else:
        final[string1[i]]=1
for x,y in final.items():
    answer.append(x)
answer="".join(answer)
print(answer)
