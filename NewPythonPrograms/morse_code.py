morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words=["gin","zen","gig","msg"]
temp=0
new_string=""
assign={}
count=0
final_assignment={}
final_count=0
for i in range(97,123):
    for j in range (len(morse_code)):
        x=chr(i)
        if x in assign:
            continue
        else:
            assign[x]=morse_code[temp]
            temp=temp+1
for k in range(len(words)):
    for l in range(len(words[k])):
        character=words[k][l]
        if character in assign and count<len(words[k]):
            count=count+1
            new_string=new_string+assign[character]
            if count==len(words[k]):
                count=0
                break
    new_string=new_string+","
new_string1=new_string.split(",")
longer=len(new_string1)
trimmer=new_string1[0:longer-1]
for x in trimmer:
    if x in final_assignment:
        final_assignment[x]=final_assignment[x]+1
    else:
        final_assignment[x]=1
for key1,value1 in final_assignment.items():
    final_count=final_count+1
print(final_count)

    