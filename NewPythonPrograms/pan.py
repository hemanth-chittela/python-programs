string="abca"
another_string=list(string)
listing=list(string)
if string==string[::-1]:
    print("true")
else:
    for i in range(len(listing)-1,-1,-1):
        listing.pop(i)
        x1=another_string.pop(i)
        listing="".join(listing)
        another_string="".join(another_string)
        if listing==another_string[::-1]:
            print("true")
        else:
            temp=list(another_string)
            temp.append(x1)
            x=temp
            print(x)
            temp1=list(listing)
            temp1.append(x1)
            y=temp1
            print(y)
    









    #x=list(listing.pop(listing[i]))
    #listing=listing.pop(listing[i])
    #x="".join(x)
    #listing="".join(x)
    #if x==listing:
    #    print("True")
    #else:
    #    print("False")

