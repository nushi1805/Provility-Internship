#FUNCTIONS
#Function is a block of code that performs a specific task
#Function is declared using 'def' keyword
#It makes the code reusable and organized
#syntax = def function_name (parameters):
def greet(name):
    print("hello",name)

greet("Anusha") #A function can be called with its name followed by parentheses with parameters

#FUNCTION TO SQUARE ELEMENTS IN THE LIST
def squares(my_list):
  square=[]
  for i in my_list:
      square.append (i**2)
  return square
list = [9,5,7,5,11]
result = squares(list)
print(result)

#Default args - Here the parameters have a predefined value.
#During function call when the parameter is not defined this default value is used.
def function (num1, num2 = 30):
    print("1st number =" ,num1)
    print("2nd number =", num2)

function(90)
function(20 , 70)

# Keyword Args : Arguments are passed by exclusively naming them, so that they can be passed in any order
def numbr(numA,numB):
    print("1st number =", numA)
    print("2nd number =", numB)

numbr(30,40)
numbr(numB=40 , numA=30)

#Required Args : These are arguments that must be provided when calling the function.
# If they are missing, the function will raise an error
def greet(name, age):
    print(f"Hello, {name}, you are {age} years old.")

greet("Anusha", 20)

#variable length args : These allow you to pass any number of positional arguments to a function, and they are collected into a tuple.
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Damon", "Stefan", "Klaus")


