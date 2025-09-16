#!/usr/bin/python3

import sys

def aff_rev_params():
    for arg in reversed(sys.argv[1:]):
        print(arg)

aff_rev_params()