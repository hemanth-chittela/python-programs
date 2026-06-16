days=[2,4,1]
new_list=[]
count=0
final=0
another=0
if len(days)==1:
    print("0")
elif min(days)==days[0]:
    result=max(days)-min(days)
    print(result)
else:
    for x in range(len(days)-1):
        if days[x]>days[x+1]:
            another=another+1
            if another==len(days)-1:
                print(final)
                break                          
        else:
            low=min(days)
            for i in range(len(days)):
                if low==days[i]:
                    break
                else:
                    count=count+1
                    for i in range(len(days)):
                        if i<=count:
                            continue
                        else:
                            new_list.append(days[i])
            max=max(new_list)
            final_result=max-low
            print(final_result)
            break

        

