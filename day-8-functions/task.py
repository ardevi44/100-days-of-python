def greet():
    print("Hello")
    print("How do you do?")
    print("What's the weather like today?")


# greet()

# Functions that allow for inputs


def greet_with_name(name):
    print(f"\nHello how are you today {name}")
    if len(name) > 8:
        print("Your name is too large")
    else:
        print("I like your name")


# greet_with_name("Entrepreneur")

# Function with more than 1 input


def greet_with(name, location):
    print(f"Hi {name.split()[0]}, what is it like in {location.split(",")[0]}")


# This is a positional argument behavior, it means if i change the order of the arguments
# the greeting changes its meaning.
# greet_with("The middle of nowhere, Kansas city", "Courage the cowardly dog") <- The order has changed

# A way to avoid the positional argument behavior are the keyword arguments
# Like this ...
greet_with(location="The middle of nowhere, Kansas city",
           name="Courage the cowardly dog")
