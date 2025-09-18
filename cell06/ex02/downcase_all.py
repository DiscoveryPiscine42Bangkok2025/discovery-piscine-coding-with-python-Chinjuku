#!/usr/bin/python3

import sys

def downcase_it():
    if len(sys.argv) > 1:
        for txt in sys.argv[1:]:
            print(txt.lower())
    else:
        print("none")

downcase_it()