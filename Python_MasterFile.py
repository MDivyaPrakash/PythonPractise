#!/usr/bin/env python3
#This below program contains the basic command and concepts of the python language.
def prntn(inp):
    print("This is the output -->  {}".format(inp))
    print("======================")
print('Hello World')
x=1
z=2
prntn(x)
print("This is the output -->  {},{}".format(x,z))
prntn(type(x))
#Boolean
y = True
#prntn(y)
# Basic If-else
if (y):
    prntn(y)
else:
    prntn(x)
#Sequence Types
#List( Sequence of any type) . For loop can also be used to print these.
L = [1,2,'Divya list',4]
prntn(L)
#prntn(L[0])
#Tuple is like a list , but it is immutable meaning we cannot change the value.
T = (1,2,'Divya Tuple',4)
prntn(T)
prntn(T[3])
#Range range(x , y , z)  x is start , y is end, z is step size.range(n) == 0 to n
rr = range (5)
for i in rr:
    print(' The loop number is {}'.format(i))
R = range(5 , 12 , 5)
for i in R:
    print(' The second loop number is {}'.format(i))
#Dictionary --> it is mutable
Dict = {'one': 1, 'bro' : 2 , 'trek' :3}
for j,h in Dict.items():
    print('Key is {} and value is {}'.format(j,h))
#ID function gives out a unique number for the given object
Id1 = (1,2,'Divya Tuple',4)
Id2 = (1,2,'Divya Tuple',4)
print(id(Id1))
print(id(Id2))
#Id number of same value is equal but same tuple or objects with same values do not have same ID.
if Id1[0] != Id2[0]:
    print("Yeah")
elif Id1 is Id2:
    print("Nope")
# In IF is is used for values and isintance is used to compare the type.

