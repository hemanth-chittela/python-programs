total=0
number=int(input("enter the number: "))
to_string=str(number)
for i in to_string:
    s=int(i)
    total=total+s**len(to_string)
if total==number:
    print("armstrong",number)
else:
    print("not armstrong",number)

