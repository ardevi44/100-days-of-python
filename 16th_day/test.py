class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_1 = Person("ardevi", 23)

print(id(person_1))
print(person_1 is person_1)
