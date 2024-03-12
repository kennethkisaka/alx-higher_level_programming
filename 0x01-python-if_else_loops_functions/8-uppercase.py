#!/usr/bin/python3
def uppercase(str):
    for i in list(str):
        if ord(i) <= 122 and ord(i) >= 97:
            print("{:s}".format(chr(ord(i) - 32)), end="")
        else:
            print("{:s}".format(i), end="")
