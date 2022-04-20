import argparse

ap = argparse.ArgumentParser()

ap.add_argument('-a',
                '--first_operand',
                required=True,
                help='first operand')
ap.add_argument('-b',
                '--second_operand',
                required=True,
                help='second_operand')

args = vars(ap.parse_args())

a = int(args['first_operand'])
b = int(args['second_operand'])

print('Sum is {}'.format(a + b))
print('Sub is {}'.format(a - b))
print('Div is {}'.format(a / b))
print('Mul is {}'.format(a * b))


# python3 script_5.py -a 5 -b 5 // for run short form
# python3 script_5.py --first_operand 5 --second_operand 5 // for run long form
# python3 script_5.py --help // for run help


