#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print("0 and is zero")
elif number % 10 > 5:
    print(f"{number % 10} and is greater than 5")
else:
    print(f"{number % 10} and is less than 6 and not 0")
