#!/usr/bin/env python3

def i_got_that():
    input("What you gonna say? : ")
    while True:
        text = input("I got that! Anything else? : ")
        if (text == "STOP"):
            break

i_got_that()