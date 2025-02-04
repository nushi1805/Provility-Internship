#PYTHON VARIABLES
#No need to use data types while initializing variabkles

x= 24
print(x)

# python is a dynamic lang. meaning a variable can hold multiple values during execution
# It works in a sequential way

x = "cat"
x =18
print(x)

x , y, z = 1 , 2, 3
print (x,y,z) #Python allows multiple variables to be assigned values in a single line

p = 2
q = x
p = 3
q = 4
print("P =" ,p ,"Q=" ,q)
"""Note: python works in a sequential manner(dynamic programming), the recently declared one is considerd. 
The one which hasbeen overwritten is considered as garbage"""

# Tuple unpacking - Allows to assign multiple values in single line can be used for swapping without the use of temp variable
a , b = 10 , 5 #packs 10 and 15 into a tuple (10, 5) and unpacks them into a and b
a , b = b , a
print(a,b)

#swapping with temp variable- temp variable  is a temporary storage used to hold a value temporarily during the swapping process.
#temp safely holds the value of a until you assign it back to b
a = 10
b = 5
temp = a
a = b
b = temp
print (a,b)

#Global and local Variable
"""The scope of a variable determines where it can be accessed. 
Local variables are scoped to the function in which they are defined, while global variables can be accessed throughout the program. 
Note: Local vs Global Variables Without global: Variables inside a function are local and do not affect variables outside the function.
With global: The function modifies the global variable directly, and changes are reflected everywhere."""
x = 10

def localglobal():
    x = 20
    print(x)

localglobal()

print (x)

x = 10

def localglobal():
    global x
    x = 20
    print(x)

localglobal()

print (x)