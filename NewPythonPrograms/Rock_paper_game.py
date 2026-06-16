#Rock_paper_Scissors_Game
import random
Hands_Gestures=["Rock","Paper","Scissors"]
Computer_choice=random.choice(Hands_Gestures)
Human_Choice=str(input("Give the following Either Rock Or Paper Or Scissors: "))
print("Computer has chosen",Computer_choice)
if (Human_Choice=="Rock" and Computer_choice=="Rock") or (Human_Choice=="Paper" and Computer_choice=="Paper") or (Human_Choice=="Scissors" and Computer_choice=="Scissors"):
    print("It is a tie")
elif Human_Choice=="Rock" and Computer_choice=="Paper":
    print("Paper won by Computer and you lost")
elif Human_Choice=="Paper" and Computer_choice=="Rock":
    print("Paper won by Human")
elif Human_Choice=="Scissors" and Computer_choice=="Paper":
    print("Scissors won by Human")
elif Human_Choice=="Paper" and Computer_choice=="Scissors":
    print("Scissors won by Computer and you lost")
elif Human_Choice=="Scissors" and Computer_choice=="Rock":
    print("Rock won by Computer and you lost")
else:
    print("Rock won by human")
