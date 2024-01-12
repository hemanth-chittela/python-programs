import pyautogui
import time
text=str(input("Enter the string"))
time.sleep(5)
j=1
for i,j in enumerate(range(j,11)):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
print("number of messages sent =",j)