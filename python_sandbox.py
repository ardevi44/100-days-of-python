import random

names = ["Arbey", "Daniel", "Maria", "Ale", "Laura", "Pedro", "Mr. Fantastic"]
# Will choose some random position of the list
print(random.choice(names))


names += "Leo"  # In this case it will add letter by letter
# This will add to the list element by element, remember names is mutable
names += ["Norma", "John"]

print(names)
