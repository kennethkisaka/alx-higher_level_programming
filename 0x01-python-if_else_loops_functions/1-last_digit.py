#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    n = number  * -1
digit = n % 10
print(digit)
if digit == 0:
    print(f"Last digit of {number} is 0 and is zero")
elif digit:
    print(f"Last digit of {number} is {digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
