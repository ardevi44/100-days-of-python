# The challenge is to generate a password, with a random letters, symbols and numbers from those lists based on the
# user inputs.
# And in a random order, example, you could find a letter first then a symbol, then another symbol, then a number etc.

# 1. *** Easy level ***
# There is a easy level of this challenge which is group the characters, first the group of letters, then the group
# of numbers and then the group of symbols.
# 2. *** Hard level ***
# 2. Obviously the main way is do it like the beginning explanation, ALL PASSWORD IN A RANDOM ORDER.

# Lets take a look to the possible algorithm.
# -------------------------------------------

# 1. Take a number of letters, symbols and numbers
# 2. That number will be the number of times i going to take randomly a letter or symbol from the lists respectively and summarize
# all this characters in a password variable
# *Hard level
# 3. Take randomly again certain index from the previous password and pull out the character into a new
# variable.
# 4. also you have to remove from the previous string the character you actually takes

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letters_quant = int(
    input("How many letters would you like in your password?: "))
symbols_quant = int(input("How many symbols would you like?: "))
numbers_quant = int(input("How many numbers would you like?: "))

password = ""

for letter in range(0, letters_quant):
    password += letters[random.randint(0, len(letters) - 1)]

for symbol in range(0, symbols_quant):
    password += symbols[random.randint(0, len(symbols) - 1)]

for number in range(0, numbers_quant):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(f"Total of characters in your password: {len(password)}")
print(f"Password: {password}")

final_password = ''
for current_time in range(0, len(password)):
    random_position = random.randint(0, len(password) - 1)
    final_password += password[random_position]
    password = password[:random_position] + password[random_position + 1:]

print(f"This is your final password: {final_password}")
