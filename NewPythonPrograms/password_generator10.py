import random
small_letters="abcdefghijklmnopqrstuvwxyz"
capital_letters=small_letters.upper()
numbers="1234567890"
special_characters="!@#$%^&*()_+{}:<>|"
combined=small_letters+capital_letters+numbers+special_characters
length=16
password="".join(random.sample(combined,16))
print("the password is",password)