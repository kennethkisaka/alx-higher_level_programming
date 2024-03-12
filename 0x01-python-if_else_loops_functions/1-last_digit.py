#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])
if digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif digit < 6 or number < 0:
    if number < 0:
        print(f"Last digit of {number} is -{digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {digit} and is greater than 5")
