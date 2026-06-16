word1="ab"
word2="pqrs"
final=[]
if len(word1)==len(word2):
    for i in range(len(word1)):
            final.append(word1[i])
            final.append(word2[i])
else:
    if len(word1)>len(word2):
        try:
            for j in range(len(word1)):
                final.append(word1[j])
                final.append(word2[j])
        except:
                j=j+1
                for j in range(j,len(word1)):
                    final.append(word1[j])
    else:
        try:
            for k in range(len(word2)):
                final.append(word1[k])
                final.append(word2[k])
        except:
                final.append(word2[k])
                k=k+1
                for k in range(k,len(word2)):
                    final.append(word2[k])
final="".join(final)
print(final)