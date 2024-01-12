import random
import string

lower=string.ascii_lowercase
upper=lower.upper()
length=16
numbers="0123456789"
special_characters="!@#$%^&*()_+<>?:[]"
string=lower+upper+numbers+special_characters
password="".join(random.sample(string,length))
print("Your random password is",password)
