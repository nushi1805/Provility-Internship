# PYTHON OPERATORS
# Operators are special symbols or keywords used to perform operations on values and variables.
# Types of operators in Python:
# - Arithmetic Operators
# - Assignment Operators
# - Comparison Operators
# - Logical Operators
# - Bitwise Operators
# - Membership Operators
# - Identity Operators

# 1. Arithmetic Operators
# Used for performing basic arithmetic operations.
x = 10
y = 3
print("Addition:", x + y)  # Adds x and y
print("Subtraction:", x - y)  # Subtracts y from x
print("Multiplication:", x * y)  # Multiplies x and y
print("Division:", x / y)  # Divides x by y (floating-point division)
print("Floor Division:", x // y)  # Divides x by y and rounds down to the nearest integer
print("Modulus:", x % y)  # Remainder when x is divided by y
print("Exponentiation:", x ** y)  # x raised to the power of y

# 2. Assignment Operators
# Used to assign values to variables. Can combine with arithmetic operators.
a = 5
a += 3  # Same as a = a + 3
print("a after += 3:", a)
a *= 2  # Same as a = a * 2
print("a after *= 2:", a)

# 3. Comparison Operators
# Used to compare two values. Returns True or False.
x = 10
y = 5
print("x == y:", x == y)  # Checks if x is equal to y
print("x != y:", x != y)  # Checks if x is not equal to y
print("x > y:", x > y)  # Checks if x is greater than y
print("x < y:", x < y)  # Checks if x is less than y
print("x >= y:", x >= y)  # Checks if x is greater than or equal to y
print("x <= y:", x <= y)  # Checks if x is less than or equal to y

# 4. Logical Operators
# Used to combine conditional statements.
a = True
b = False
print("a and b:", a and b)  # True if both are True
print("a or b:", a or b)  # True if at least one is True
print("not a:", not a)  # Negates the value of a

# 5. Bitwise Operators
# Used to perform operations at the bit level.
x = 4  # Binary: 0100
y = 5  # Binary: 0101
print("x & y:", x & y)  # AND operation: 0100 & 0101 = 0100 (4)
print("x | y:", x | y)  # OR operation: 0100 | 0101 = 0101 (5)
print("x ^ y:", x ^ y)  # XOR operation: 0100 ^ 0101 = 0001 (1)
print("~x:", ~x)  # NOT operation: ~0100 = -(0100 + 1) = -5
print("x << 1:", x << 1)  # Left shift: 0100 << 1 = 1000 (8)
print("x >> 1:", x >> 1)  # Right shift: 0100 >> 1 = 0010 (2)

# 6. Membership Operators
# Used to check for membership in sequences (like lists, tuples, strings).
my_list = [1, 2, 3, 4]
print("3 in my_list:", 3 in my_list)  # True if 3 is in my_list
print("5 not in my_list:", 5 not in my_list)  # True if 5 is not in my_list

# 7. Identity Operators
# Used to compare memory locations of two objects.
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]
print("a is b:", a is b)  # True, both point to the same memory location
print("c is d:", c is d)  # False, different memory locations
print("c == d:", c == d)  # True, values are the same


