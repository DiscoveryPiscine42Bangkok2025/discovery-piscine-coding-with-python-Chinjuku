#!/usr/bin/python3

import sys

def append_it():
    word = "ism"
    params = sys.argv[1:]
    for i in params:
        if i[-3:] == word:
            pass
        else:
            print(i + "ism")
    
append_it()