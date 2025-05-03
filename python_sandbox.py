import os
import stickman
import random

names = ["Arbey", "Daniel", "Maria", "Ale", "Laura", "Pedro", "Mr. Fantastic"]
# Will choose some random position of the list
print(random.choice(names))


names += "Leo"  # In this case it will add letter by letter
# This will add to the list element by element, remember names is mutable
names += ["Norma", "John"]

print(names)

print(stickman.draw[0])
i = 1
while i in range(len(stickman.draw)):
    character = input("Type [n] to see the next draw: ")
    if character == "n":
        os.system("cls")
        print(stickman.draw[i])
    i += 1
