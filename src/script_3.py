import sys

number = 1

if len(sys.argv) == 2:
    number = int(sys.argv[1])

for i in range(number):
    print('Hello World!')

# python3 script_3.py 10 // for run