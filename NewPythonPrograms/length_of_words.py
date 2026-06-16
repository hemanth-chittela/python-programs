sentence="this is the best pizza ever made by the baker"
new_list=[]
new_string=sentence.split(" ")
for i in new_string:
    if len(i)>4:
        new_list.append(i)
print(new_list)