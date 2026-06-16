word=str(input("Enter the word: "))
vowels=["a","e","i","o","u"]
flag=False
for i in vowels:
    if i in word:
        flag=True
        break
if flag:
    print("it is a vowel")
else:
    print("it is a consonent")