import sys

args = sys.argv[1:]
word = "z"

if len(args) < 1:
    print("none")
else:
    count = 0
    for char in args[0]:
        if char == word:
            count += 1
    if count > 0:
        print(f"{word * count}")
    else:
        print("none")