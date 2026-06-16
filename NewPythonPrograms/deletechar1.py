#https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/33064
def new_code(string):
    count=0
    new_string=" "
    final_string=""
    new_count=0
    k=0
    for letter in range(len(string)-1):
        if string[letter]!=string[letter+1]:
            new_count=new_count+1
        else:
             continue            
    if new_count==len(string)-1:
        final_string=string
    elif len(string)==1:
            new_string=new_string+string[0]
    else:
        for i in range(len(string)-1):
            if string[i]==string[i+1]:
                if count<1:
                    if string[i] not in new_string[-1]:
                        for j in range(2):
                            new_string=new_string+string[i+1]
                            count=count+1

                    elif k<1: 
                        for k in range(1):
                            new_string=new_string+string[i+1]
                            k=k+1
                            count=count+1
                            k=0
                    else:
                            continue
            elif string[i] in new_string:
                new_string=new_string+string[i+1]
                count=0
            else:
                new_string=new_string+string[i]
                count=0
    final_string=final_string+new_string[1:]
    return final_string

s=new_code("leeetcode")
print(s)

