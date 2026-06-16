names=["flower","flow","flight"]
x=1
y=0
temp=0
count=1
final=[]
letter_count=0
if len(names)==1:
    print(names[0])
else:
    try:
        for i in range(len(names)):
            for j in range(len(names[i])):
                if i>=1:
                    break
                elif names[i][j]!=names[x][y]:
                    break
                else:
                    while names[i][j]==names[x][y]:
                        letter_count=letter_count+1
                        x=x+1
                        if letter_count+1==len(names):
                            final.append(names[i][j])
                            letter_count=0
                            y=y+1
                            x=0
                            x=x+1
                            break
    except:
        print("ignore")
    if len(final)>=1:                
        together="".join(final)
        print(together)
    else:
        print("")
