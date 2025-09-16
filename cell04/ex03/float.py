def check_float():
    num = float(input("Give me a number: "))
    if num.is_integer():
        print("The number is integer.")
    else:
        print("The number is decimal.")

check_float()