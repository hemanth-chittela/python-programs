new_string=""
s="bad"
count1=0
adding_shifts=0
final=[]
substraction=0
shifts=[10,20,30]
storage=[]
x=0
temp=0
for i in range(len(shifts)):
    adding_shifts=adding_shifts+shifts[i]
for k in range(len(shifts)):
    for j in range(97,123):
        if chr(j)==s[count1]:
            if j+adding_shifts>122:
                substraction=122-j
                adding_shifts=adding_shifts-substraction
                if substraction==0:    
                    final.append(chr(adding_shifts+96))
                    storage.append(shifts[x])
                    adding_shifts=adding_shifts+substraction
                    adding_shifts=adding_shifts-shifts[x]
                    x=x+1
                    count1=count1+1
                elif substraction>=1:
                    final.append(chr(adding_shifts+97))
                    storage.append(shifts[x])
                    adding_shifts=adding_shifts+substraction
                    adding_shifts=adding_shifts-shifts[x]
                    x=x+1
                    count1=count1+1
            else:
                final.append(chr(j+adding_shifts))
                count1=count1+1
                adding_shifts=adding_shifts-shifts[x]
                x=x+1
                break
    if count1>=len(s):
        break
final1="".join(final)
print(final1)