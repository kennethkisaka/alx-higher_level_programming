#!/usr/bin/python3
def uppercase(str):
    for i in list(str):
        if ord(i) <= 122 and ord(i) >= 97:
            letter = "{:s}".format(chr(ord(i) - 32))
        else:
            letter = "{:s}".format(i)
        print("{:s}".format(letter), end="")
    print("\n", end="")
