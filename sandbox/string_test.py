myString = "Hello, World!"

var_1 = myString[0]
var_2 = myString[7:]
var_3 = myString[1:4]

print("var_1: " + var_1)  # Output: var_1: H
print("var_2: " + var_2)  # Output: var_2: World!
print("var_3: " + var_3)  # Output: var_3: ell

# A multi-line string
my_string = """If it were done when 'tis done, then 'twere well
It were done quickly: if the assassination
Could trammel up the consequence, and catch
With his surcease success; that but this blow
Might be the be-all and the end-all here,
But here, upon this bank and shoal of time,
We'ld jump the life to come."""

print(my_string)


my_next_string = """
Choose an option:
  * Move away
  * Take some money
  * Give a hug!
  * Just leave me in peace

And remember put the \"\"\" first signs immediately after the equal sign
after write what you need. At the very bottom of the string put again the
\"\"\" signs.

This will do a better job for indentations and lists
"""

# Remember this lines bellow are treated as a comment
"""
If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.
"""

print(my_next_string)
