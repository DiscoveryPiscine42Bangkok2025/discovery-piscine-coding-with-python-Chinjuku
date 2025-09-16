def to25(num):
    if num < 25:
        while num < 25:
            print("Inside the loop, my variable is " + str(num))
            num += 1
    elif num == 25:
        print("The number is already 25")
    else:
        print("Error")

to25(int(input()))