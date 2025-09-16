def age():
    current_age = int(input("Please tell me your age: "))
    future = [10, 20, 30]
    for i in future:
        future_age = current_age + i
        print(f"In {i} years, you'll be {future_age} years old.")

age()