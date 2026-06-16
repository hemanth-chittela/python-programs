string="IceCreAm"
vowels=""
for i in string:
    if i in "aeiouAEIOU":
        vowels=vowels+i
vowels=vowels[::-1]
listing=list(string)

index=0
for character in range(len(listing)):
        if listing[character] in vowels:
            listing[character]=vowels[index]
            index=index+1
            string="".join(listing)
print(string)