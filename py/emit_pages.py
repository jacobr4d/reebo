#!/usr/bin/env python3
import sys

i = 0
for l in sys.stdin:
    if l.startswith('<PB'):
        i += 1
        print(f'<h3>Page {i}</h3>')
    print(l)
