#!/usr/bin/env python3

def advanced_mult():
    for i in range(11):
        loop_inside = ""
        for j in range(11):
            loop_inside += str(i * j) + " "
        print(f"Table de {i}: {loop_inside}")

advanced_mult()
