word=str(input("Enter the word: "))
occurance_count={}
for i in word:
    if i in occurance_count:
        occurance_count[i]+=1
    else:
        occurance_count[i]=1
print(occurance_count)
for i in occurance_count:
    if occurance_count[i]>1:
        print(i)