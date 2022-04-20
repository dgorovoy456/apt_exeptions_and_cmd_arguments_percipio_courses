try:
    file = open('testfile.txt')
    file.write('Writing to the open file')
except:
    print('Oops! Something went wrong')
else:
    print('Nothing went wrong')

try:
    file = open('testfile.txt', 'w')
    file.write('Writing to the open file')
    print('One line written to the file')
except:
    print('Oops! Something went wrong')
else:
    print('Nothing went wrong')
finally:
    file.close()

print('#######################################################\n')

# a = 5
# b = 'Hello'
# d = a + b + c
#
# print(d)
#
# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions_3.py", line 25, in <module>
#     d = a + b + c
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    a = 5
    b = 'Hello'
    d = a + b + c
except TypeError:
    print('Type Error was thrown')

try:
    a = str(5)
    b = 'Hello'
    d = a + b + c
except TypeError:
    print('Type Error was thrown')
except NameError:
    print('NameError was thrown')

try:
    a = str(5)
    b = 'Hello'
    c = int('World')
    d = a + b + c
except TypeError:
    print('Type Error was thrown')
except NameError:
    print('NameError was thrown')
except ValueError:
    print('ValueError was thrown')

print('#######################################################\n')

# number = int(input('Enter a number'))
#
# if number > 5:
#     raise Exception('The number should not exceed 5.'
#                     ' The value of number is {}'.format(number))


number = int(input('Enter a number'))
try:
    if number > 5:
        raise Exception('The number should not exceed 5.'
                        ' The value of number is {}'.format(number))
except Exception as error:
    print('Caught this Error: ' + repr(error))
