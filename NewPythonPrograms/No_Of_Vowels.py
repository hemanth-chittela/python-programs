import re
word=str(input("Enter the word: "))
if re.search("[aeiouAEIOU]",word):
    print("vowel")
else:
    print("Consonent")
count=0
for i in word:
    if re.search("[aeiouAEIOU]",i):
        print(i,end=" ")
        count=count+1
print("No of vowels",count)