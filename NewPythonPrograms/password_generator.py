import random
small_characters="abcdefghijklmnopqrstuvwxyz"
big_characters=small_characters.upper()
numbers="0123456789"
special_characters="!@#$%^&*()_+{}:<>?"
length=16
combining_strings=small_characters+big_characters+numbers+small_characters+special_characters
password="".join(random.sample(combining_strings,length))
print(password)
