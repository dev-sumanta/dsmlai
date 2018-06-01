# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:46:16 2017

@author: Samar
"""

import sys

# Built in  functions and methods
print(type(dir))


# user defined functions
def foo():
    pass


print(type(foo))

# lambda functions
a_lambda_func = lambda x: x ** 2
print(a_lambda_func(3))
print(type(a_lambda_func))


class DC:
    def a_method(self, x):
        return x ** 2


adc = DC()
print(type(adc.a_method))
print(adc.a_method(3))

print(callable(adc))
print(callable(adc.a_method))

# compile
# eval a statement
eval_code = compile('100 + 200', '', 'eval')
print(eval(eval_code))

# compile a single statement and execute
single_code = compile("print('Single code execution from compile')",
                      '', 'single')
print(single_code)
print(exec(single_code))

# group of executable statements
exec_code = compile("""
req = int(input('Count how many numbers? '))
for each_num in range(req):
   print(each_num)
""", '', 'exec')
print(exec_code)
print(exec(exec_code))

# eval
print(eval('242'))
print(int('242'))
print(eval('112 + 234'))
print(int('112 + 234'))

# exec
print(exec("print(100 + 200)"))
# exec multi line code
exec("""
from random import randint
x = randint(0,100)
print(x)
for a in range(x):
    print(a)
    if(a > 4):
        break
 """)

code_file_to_exec = open('C:\\Users\\Samar\\OneDrive\\'
                         'pycodes\\exec_code_file.py')
exec(code_file_to_exec.read())
code_file_to_exec.close()


sys.path.append('C:\\Users\\Samar\\OneDrive\\pycodes\\pymod')
exec(open('C:\\Users\\Samar\\OneDrive\\pycodes\\pymod\\channel.py').read())


print(sys.modules.keys())
