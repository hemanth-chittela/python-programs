words=["a","aa","aaa","aaaa"]
final=[]
another_filter={}
final2=[]
answer=[]
for i in range(len(words)):
    s=len(words[i])
    final.append(s)
for j in range(len(final)):
    if final[j] in another_filter:
        another_filter[final[j]]=another_filter[final[j]]+1
    else:
        another_filter[final[j]]=1
for x,y in another_filter.items():
    if y>1:
        final2.append((x,y))
if len(final2)==0:
    print(0)
else:
    answer=max(final2)
    print(pow(answer[0],2))
