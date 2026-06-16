import random

Computer_generated=random.randint(1,50)

attempts=0
guess=0

while guess!=Computer_generated:
    guess=int(input("Enter the value from the 1 to 50: "))
    attempts=attempts+1
    if guess>Computer_generated:
        print("The value you have guessed is greater then computer generated")
    elif guess<Computer_generated:
        print("The value you have guessed is less than Computer Generated")
    else:
        print("You have taken",attempts,"attempts and it is correct")

