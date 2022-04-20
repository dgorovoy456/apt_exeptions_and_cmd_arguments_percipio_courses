import time

try:
    time.sleep(111)
except KeyboardInterrupt:
    print('KeyboardInterrupt has occurred')

print('#############################################################\n')

try:
    f = open('nonexistent_file')
except OSError:
    print('OS Error')
except FileNotFoundError:
    print('File not found Error')

try:
    f = open('nonexistent_file')
except FileNotFoundError:
    print('File not found Error')
except OSError:
    print('OS Error')

print('#############################################################\n')

try:
    print(var)
except NameError:
    print('The variable has not been defined')
finally:
    print('The "try except block" ended')

var = 'xyz'

try:
    print(var)
except NameError:
    print('The variable has not been defined')
finally:
    print('The "try except block" ended')

print('#############################################################\n')

try:
    file = open('testfile.txt', 'w')
finally:
    file.close()
    print('Done with processing the file')




