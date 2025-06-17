# Datatypes in Python

some_number = 1234567

# Some text to print in the console
str_message = "The number " + \
    str(some_number) + " is made by " + str(len(str(some_number))) + " digits"

# We can do this better with format strings by doing this ...
f_str_message = f"The number {some_number} is made by {len(str(some_number))} digits"

# Checking the type of some values
print(type(f_str_message))
print(type(345))
print(type(True))
print(type(23.45))

some_other_number = 23
print(isinstance(some_other_number, str))


# Integer = whole number
print(123 + 345)

# Large Integer
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# String
print("Hello")
print("The last character -> " + "Hello"[4])

# Python built-in functions
# Variables declaration
# -------------------------
# Here we are using some of the built-in functions inside of python language.
# - len()
# - str()
# - type()
# - isinstance()

# Comparison Operators
# -----------------------
# >   greater than
# <   less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to

# Modulo Operator
# ________________________
# Modulo operator % -> tells us the remaining of a division
#
