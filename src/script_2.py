import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-display')
args = parser.parse_args()

print(args.display)

# python3 script_2.py -display 'lool' // for run
