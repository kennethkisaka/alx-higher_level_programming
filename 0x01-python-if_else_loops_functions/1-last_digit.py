#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number % 10 == 0:
    print(f"Last digit of {number} is 0 and is zero")
elif number % 10 > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
