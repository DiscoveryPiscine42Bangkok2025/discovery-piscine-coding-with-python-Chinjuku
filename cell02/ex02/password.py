def password():
    pwd = input()
    my_password = "Python is awesome"
    if pwd == my_password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

password()