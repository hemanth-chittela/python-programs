string=""
if len(string)>1 or (" " in string): 
    string=string.split(" ")
    string=len(string)
    print(string)
elif len(string)==1:
    print(1)
else:
    print(0)