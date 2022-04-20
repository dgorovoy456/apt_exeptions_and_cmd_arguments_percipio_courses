# print(variable)

# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions_1.py", line 2, in <module>
#     print(variable)
# NameError: name 'variable' is not defined

try:
    print(variable)
except:
    print('Exeption occurred(Name Error), because "variable" was not defined')

print('######################################################################\n')

try:
    print(variable)
except NameError:
    print('Variable is not defined')
except:
    print('Unknown error has occurred')

print('######################################################################\n')

# f = open('nonexistent_file')
#
# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions_1.py", line 24, in <module>
#     f = open('nonexistent_file')
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file

try:
    f = open('noneexistent_file')
except FileNotFoundError:
    print('No such file')
except:
    print('An unknown error has occurred')

print('######################################################################\n')

# input_var = int(input('Please enter a number'))
#
# Please enter a numberew
# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions_1.py", line 40, in <module>
#     input_var = int(input('Please enter a number'))
# ValueError: invalid literal for int() with base 10: 'ew'

while True:
    try:
        input_var = int(input('Please enter a number'))
        break
    except ValueError:
        print('Oops! That was not a valid number. Try again...')

print('######################################################################\n')


attempts = 0

while True:
    try:
        input_var = input('Please enter a number')
        input_var = int(input_var)

    except ValueError:
        attempts += 1

        if attempts < 3:
            print('Oops! That was not a valid number. Try again...')
        else:
            print('You really want to input string? Fine we`ll handle it')
            input_var = str(input_var)
            print(input_var)
            break



