# !/usr/bin/env python3

def up_low(text):
    for char in text:
        if char.islower():
            print(char.upper(), end="")
        elif char.isupper():
            print(char.lower(), end="")
        else:
            print(char, end="")
    print()

up_low(input())