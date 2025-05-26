def greet():
    print("Hello")
    print("How do you do?")
    print("What's the weather like today?")


greet()

# Functions that allow for inputs


def greet_with_name(name):
    print(f"\nHello how are you today {name}")
    if len(name) > 8:
        print("Your name is too large")
    else:
        print("I like your name")


greet_with_name("Entrepreneur")
