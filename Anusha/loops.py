# PYTHON LOOPS
# Loops are used to execute a block of code repeatedly as long as a condition is met.
# Types of Loops:
# - for loop
# - while loop
# Python also supports control statements like break, continue, and pass to manage loop execution.

# 1. FOR LOOP
# Used to iterate over a sequence (like lists, tuples, strings, or ranges).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list

for letter in "Python":
    print(letter)  # Prints each letter in the string

# range(start, stop, step) generates numbers within a range
for i in range(1, 6):  # start=1, stop=6 (exclusive), step=1
    print(i)  # Prints numbers from 1 to 5

for i in range(10, 0, -2):  # Decrement by 2
    print(i)  # Prints 10, 8, 6, 4, 2

# Nested for loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")

# 2. WHILE LOOP
# Repeats as long as the condition is True.


x = 1
while x <= 5:
    print(x)
    x += 1  # Increment x to avoid infinite loop

#Using break in while loop
x = 1
while x <= 10:
    if x == 5:
        break  # Exits the loop when x equals 5
    print(x)
    x += 1

#Using continue in while loop
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skips the rest of the code when x equals 3
    print(x)  # Will not print 3

#Infinite loop can be stopped with ctrl+c

# 3. LOOP CONTROL STATEMENTS
# break: Terminates the loop prematurely.
# continue: Skips the current iteration and moves to the next iteration.
# pass: Does nothing and is used as a placeholder.

#pass in a loop
for i in range(5):
    if i == 3:
        pass  # Placeholder; does nothing
    print(i)


