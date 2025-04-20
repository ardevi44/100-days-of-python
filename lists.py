import random

america_states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho"
]
# Lists in python are treated as Mutable arrays

print(america_states[0])
print(america_states[1])
print(america_states[2])

# america_states[2] = "Guatemala"
# print(america_states)

# Counting by the end
# The last item is -1
print(f"last item in the list: {america_states[-1]}")  # "Idaho"
print("And so on and so far ...")
print(america_states[-2])
print(america_states[-3])

# You can append items too
america_states.append("Illinois")
print(america_states)

# Or you can extend the list
america_states.extend(["Indiana", "Iowa"])
# print(america_states)
print(f"Now the last one is: {america_states[-1]}")
america_states.extend(["Kansas", "Kentucky", "Louisiana", "Maine", "Maryland"])
print(america_states)
print(f"Now the last one is: {america_states[-1]}")

'''
You don't have to memorize all the methods of lists
Why we have google? Because there are a lot information that we can't memorize.
instead you should memorize what kind of things you can do with that data structure then, you can look
for it in the internet. And that's all
'''

# Just a practice ...
"""
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

i = 0
alice = 0
bob = 0
charlie = 0
david = 0
emmanuel = 0

print('''
Friends occurrence
------------------''')
while i < 10:
    current_name = friends[random.randint(0, 4)]
    print(f"{i+1} -> {current_name}")
    i += 1
    if current_name == friends[0]:
        alice += 1
    elif current_name == friends[1]:
        bob += 1
    elif current_name == friends[2]:
        charlie += 1
    elif current_name == friends[3]:
        david += 1
    else:
        emmanuel += 1

"""

# print(f"""
# Frequency
# ---------
# {friends[0]}: {alice}
# {friends[1]}: {bob}
# {friends[2]}: {charlie}
# {friends[3]}: {david}
# {friends[4]}: {emmanuel}
# """)
