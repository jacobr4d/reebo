import sys

for line in sys.stdin:
    for word in line.split():
        if word == '§':
            print()
        print(word, end=' ')
    print()
