bills=[5,5,5,20,10,10]
five_dollar_count=0
ten_dollar_count=0
twenty_dollar_count=0
true_false=[]
Flag=False
for i in range(len(bills)):
    if bills[i]==5:
        five_dollar_count=five_dollar_count+1
    elif bills[i]==10:
        ten_dollar_count=ten_dollar_count+1
    elif bills[i]==20:
        twenty_dollar_count=twenty_dollar_count+1

print("five",five_dollar_count)
print("ten",ten_dollar_count)
print("twenty",twenty_dollar_count)

for j in range(len(bills)):
    if bills[j]==5:
        Flag=True
        continue
    elif bills[j]==10:
        five_dollar_count=five_dollar_count-1
        Flag=True
    elif bills[j]==20:
        ten_dollar_count=ten_dollar_count-1
        five_dollar_count=five_dollar_count-1
        Flag=True

if five_dollar_count>=0:
     Flag=True
     true_false.append(str(Flag))
else: 
    Flag=False
    true_false.append(str(Flag))
    
if ten_dollar_count>=0:
     Flag=True
     true_false.append(str(Flag))
else:
    Flag=False
    true_false.append(str(Flag))

for x in true_false:
    if x=="False":
        Flag=False
        break
    else:
        Flag=True
if Flag:
    print("true")
else:
    print("false") 

