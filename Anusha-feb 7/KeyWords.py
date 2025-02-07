#KEY WORDS

"""KEYWORDS are special words that have specific meaning and purpose in the language
It cannot be used as a name for any function or variables

True	False	None	and
or	not	is	if
else	elif	for	while
break	continue	pass	try
except	finally	raise	assert
def	return	lambda	yield
class	import	from	in
as	del	global	with
nonlocal	Async	Await """

import keyword
print(keyword.kwlist)

#Value keywords - True , false , none , del

"""True ,False - Boolean values 
true =1 , False= 0 
In conditions, True returns 1, and False returns 0 when used in arithmetic or logical operations, such as True + True = 2 or False + True = 1. 
the block continues to get executed if the condition is true"""

print(False == 0)
print(True == 1)
print(False == 1)
print(True == 0)
print(True + True + False)
print(None == None)
print(None != 0)

"""AND , OR , NOT KEYWORDS
and Keyword – return ‘True’ if both the operands are ‘True’
or Keyword – return ‘True’ if at least one operand is ‘True’
not keyword – returns ‘True’ if the expression is ‘False’, and vice versa."""

x = [1, 2, 3]
y = x

# Check the memory address (id) of both variables
print(id(x))  # Output: some memory address, e.g., 140247278158848
print(id(y))  # Output: same memory address as x, e.g., 140247278158848

# Check if they refer to the same object in memory
print(x is y)  # Output: True (since they refer to the same object)


#In key word - cheks if a value exists in the given sequence
#Is key word - checks if the both the variables  point to the same object in memory

if 's' in 'Anusha':
    print ( "lala")

a = 10
b = a  # Define b as a

print(a is b)  # True, since b and a refer to the same object (10)

a = 20
b = 30

print(a is b)  # False, a and b refer to different objects (20 and 30)

a = 20
c = 20

print(a is c)  # True, Python optimizes and reuses memory for immutable integer

