#!/usr/bin/python3

import sys

def free_range():
    if len(sys.argv) != 3:
        return "none"
    else:
        array = []
        first_params = int(sys.argv[1])
        last_params = int(sys.argv[2])+1
        for i in range(first_params, last_params):
            array.append(i)
        return array

print(free_range())