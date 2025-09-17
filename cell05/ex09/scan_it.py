#!/usr/bin/python3

import sys, re

print(len(re.findall(sys.argv[1], sys.argv[2])))

