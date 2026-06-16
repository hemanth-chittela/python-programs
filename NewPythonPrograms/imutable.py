#example to say that string is immutable so we made string to list then changed to string
string="hello"
string=list(string)
string[1]="p"
new_string="".join(string)
print(new_string)