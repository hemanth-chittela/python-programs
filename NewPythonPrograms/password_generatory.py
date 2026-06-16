import random

alphabets="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
Special_characters="!@#$%^&*(){},./|;"
combining_all=alphabets+numbers+Special_characters
length=20
password="".join(random.sample(combining_all,length))
print("Your random password Generated is:",password)