import math

def round_up():
    number = float(input("Give me a number: "))
    rounded_up_number = math.ceil(number)
    return rounded_up_number

print(round_up())