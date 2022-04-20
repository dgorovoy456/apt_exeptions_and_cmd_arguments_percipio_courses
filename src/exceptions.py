# print(variable)

# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions.py", line 2, in <module>
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
#   File "/home/dhorovyi/percipio_training/apt_exeptions_and_cmd_arguments_percipio_courses/src/exceptions.py", line 24, in <module>
#     f = open('nonexistent_file')
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file

try:
    f = open('noneexistent_file')
except FileNotFoundError:
    print('No such file')
except:
    print('An unknown error has occurred')
