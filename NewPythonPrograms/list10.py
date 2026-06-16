#testing the friend's code
string="HELLO WORLD"
l=[[i,char] for i,char in enumerate(string) if char.lower() in ["a","e","i","o","u"]]
revers=l[::-1]
print(revers)
new_thing={}

for i in range(len(revers)):
    index=l[i][0]
    print(index)
    value=revers[i][1]
    print(value)
    new_thing[index]=value
    #new_thing.update({index:value})
    print(new_thing)

