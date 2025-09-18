#!/usr/bin/python3

from checkmate import checkmate

def main():
    board = """\
....
....
....
....\
"""
    checkmate(board)

#     board = """\
# K.
# ..\
# """
#     checkmate(board)

if __name__ == "__main__":
    main()