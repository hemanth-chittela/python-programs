#Capitalize the tile (Finally did this. This will really help me in realtime)
new_string=""
string="capiTalIze tHe titLe"
list1=string.split(" ")
for j in list1:
    if len(j)>=3:
        new_string=new_string+j[0].upper()+j[1:].lower()+" "
    else:
        #new_string=new_string+""+j.lower()+" "
        new_string=new_string+j.lower()+" "
print(new_string.strip())