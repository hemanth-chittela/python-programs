n=5
counte=0
count=0
symbols=["*","/","+","-"]*n
new=[]
final_string=""
if n==1:
    print(1)
else:
    for i in range(n-1,0,-1):
        if i==0:
            break
        elif symbols[count]=="*" and counte<1:
            new.append(f"{n}*{i}")
            count=count+1
            counte=counte+1
        elif symbols[count]=="*":
            new.append(f"*{i}")
            count=count+1
        elif symbols[count]=="/":
            new.append(f"/{i}")
            count=count+1
        elif symbols[count]=="+":
            new.append(f"+{i}")
            count=count+1
        elif symbols[count]=="-":
            new.append(f"-{i}")
            count=count+1

    for x in new:
        final_string=final_string+x
    print(final_string)
    fin=eval(final_string)
    print(round(fin))

    

