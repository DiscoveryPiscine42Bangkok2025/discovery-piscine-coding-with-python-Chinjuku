def calculator():
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))

    print("Thank you!")
    print(f"{num1} + {num2} = {int(num1 + num2)}")
    print(f"{num1} - {num2} = {int(num1 - num2)}")
    if num2 != 0:
        print(f"{num1} / {num2} = {int(num1 / num2)}")
    else:
        print(f"{num1} / {num2} = Error!")
    print(f"{num1} * {num2} = {int(num1 * num2)}")

calculator()