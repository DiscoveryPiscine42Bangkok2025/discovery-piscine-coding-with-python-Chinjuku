#!/usr/bin/python3

def greetings(params = ""):
    if params == "":
        print("Hello, noble stranger.")
    elif type(params) == str:
        print(f"Hello, {params}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)