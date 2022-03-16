#!/usr/bin/env python3
# Functions
import sys


def main():
    kitten('hello','there')

def kitten(*args):
    print(args[1])
    print(f"args is {args[0]}")
# Special type of calling. Sometimes the function returns none value too if nothing is mentioned.
if __name__ == '__main__': main()

# Generators are also a special kind of function , where multiple return values is required
# In python everything is object
# Decorator is just calling the function with the argument(Weird way though)
# Keyword arguments are expecting a dictionary as their input
def F1(f):
    print('A')
    def F2():
        print('B')
        f()
        print('C')
    print('D')
    return F2
@F1
def F3():
    print('E')
F3()
# Dictionary Example
x = {'1':'Hello','2':"there"}
print(x['1'])

#Class.
# Self is a reference to the object
#The 'self' variable always refers to the object instance of a class.
#The argument is automatically filled when the method is called.
class Duck:
    sound = 'What is Class'
    def quack(self):
        print(self.sound)
# Calling via objects
donald = Duck()
donald.quack()
#Function inside the class is called a method
#iterator is a class that provides seq of items
# Handling Exceptions -ValueError - ZeroDivisionError
#Like exception in sql

try:
    x = int('kk')
except ValueError:
    print('I caught')
    print(f'The error : {sys.exc_info()}')

#String Operation, lower, upper, capitalize, split, join
print("hello".upper())
s1 = "Test"
s2 = "tEST"
print(s1 + s2)
print(s1.title())
a=1

#File Operation(open function returns a file object)
#infile = open('lines.txt',rt) wb,rb for binary ( Eg: for images)
#repr is represents the variable or string. Used in classes
print(repr(s1))

#import os for os related stuff(Modules)
#We can create our own modules(to be done)

#db api is there.(SQL lite is used).
#Usually in python , before a method the comments are added.
#Writing modules is a key



