#!/usr/bin/python3

import sys

def shrink(txt):
    # 
    return txt[:8]

def enlarge(txt, addZ):
    return txt + "Z"*addZ
    
def methods_everywhere():
    for txt in sys.argv[1:]:
        if len(txt) == 8:
            print(txt)
        elif len(txt) < 8:
            print(enlarge(txt, 8-len(txt)))
        else:
            print(shrink(txt))
        
methods_everywhere()