import random

while True:
    number=int(input("guess the number: "))
    guess=random.randint(1,6)
    if guess!=number:
        print("try again the number is",guess)
    else:
        print("yes you are right",guess)