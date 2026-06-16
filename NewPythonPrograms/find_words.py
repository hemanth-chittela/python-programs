words=words = ["aa","aaa"]
chars = "aaa"
new_string=""
length=0
count=0
for i in range(len(words)):
    for j in range(len(words[i])):
        for ch in chars:
            if len(words[i])>count:
                if ch==words[i][count]:
                    new_string=new_string+ch
                    count=count+1
                    if new_string==words[i]:
                        length=length+len(new_string)
                        new_string=new_string.replace(new_string,"")
                        count=0
                        i=i+1
                    break
print(length)
