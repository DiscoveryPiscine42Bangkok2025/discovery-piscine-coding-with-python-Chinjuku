def isneg(num):
    if num < 0:
        print("The number is negative.")
    elif num == 0:
        print("The number is both positive and negative.")
    else:
        print("The number is positive.")

isneg(int(input()))