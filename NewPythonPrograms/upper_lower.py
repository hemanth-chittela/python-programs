string="this is the best award you are ever gonna receive"
new_list=""
string=string.split(" ")
for i in range(len(string)):
    for j in range(len(string[i])):
        print(len(string[i]))
        if len(string[i])>1:
            new_list=new_list+string[i][0].upper()+string[i][1:len(string[i])-1].lower()+string[i][-1].upper()+" "
            break
        else:
            new_list=new_list+string[i][0].upper()+" "
            break
print(new_list)
            


            