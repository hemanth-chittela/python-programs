name="LeetcodeHelpsMeLearn" 
spaces=[8,13,15]
final_string=""
count=-len(spaces)
for j in range(len(name)):
    if spaces[count]==j:
        count=count+1
        final_string=final_string+" "+name[j]
    else:
        final_string=final_string+name[j]
print(final_string)            
