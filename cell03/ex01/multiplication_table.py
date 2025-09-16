#!/usr/bin/env python3

def multiplication_table(num):
    for i in range(10):
        print(f"{i} x {num} = {i * num}")

multiplication_table(int(input()))