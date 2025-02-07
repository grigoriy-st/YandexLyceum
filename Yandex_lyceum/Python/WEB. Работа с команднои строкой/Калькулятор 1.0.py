import sys

if len(sys.argv) >= 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print(0)
