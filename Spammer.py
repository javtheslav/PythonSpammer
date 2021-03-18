import keyboard
import time
from random import seed
from random import randint

    # Author = Java
    # Name = Spammer

seed(1)
x = 1
print("Type in %random% for a random number between 100000 and 999999")
print("-------------------")
time.sleep(0.5)
print("What should I spam?")
text = input()
print("How many times should I spam it?")
y = input()
print("Set the Interval:")
interval = input()
print(". . .")

output = text
random = randint(100000, 999999)

time.sleep(5)
while x < int(y):
    if text == "%random%":
        output = random
        random = randint(100000, 999999)
    keyboard.write(str(output))
    keyboard.press('enter')
    print(x)
    x = x + 1
    time.sleep(float(interval))
    if text == "%random%":
        output = random
        random = randint(100000, 999999)
    if keyboard.is_pressed('alt + w'):
        break
    
    
keyboard.write(str(output))
keyboard.press('enter')
print(x)