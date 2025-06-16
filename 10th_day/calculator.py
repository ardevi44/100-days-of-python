number_1 = None
number_2 = None


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
op_selected = None
first_calculate = True
still_calculating = True
result = None


def ask_number(result):
    """Checks which global variable should be assign number_1 or number_2
    - assign a float input to number_2 if it's none and if there is number_1
    - if there is some result assign it to number_1
    - if there isn't number_1 assigns the float input
    """
    global number_1
    global number_2

    # If is there a result assign it to a number 1
    if number_2 == None and number_1 != None:
        number_2 = float(input("Enter a number: "))
    elif result:
        number_1 = result
    elif number_1 == None:
        number_1 = float(input("Enter a number: "))


def pick_an_operation():
    """Show a list of operations to choose
    if the option is not in the list of operations it will ask to choose again
    """
    global operations
    global op_selected
    while op_selected not in operations:
        last_char = ", "
        print("pick an operation ", end="")
        for i, (op_symbol, operation) in enumerate(operations.items()):
            if i == len(operations) - 1:
                last_char = "  : "
            print(op_symbol, end=last_char)
        op_selected = input()


def perform_operation(op):
    """
    """
    global number_1
    global number_2
    global result
    global op_selected

    if op == "+":
        result = operations["+"](number_1, number_2)
        print(f"{number_1} + {number_2} = {result}")
    elif op == "-":
        result = operations["-"](number_1, number_2)
        print(f"{number_1} - {number_2} = {result}")
    elif op == "*":
        result = operations["*"](number_1, number_2)
        print(f"{number_1} * {number_2} = {result}")
    elif op == "/":
        result = operations["/"](number_1, number_2)
        print(f"{number_1} / {number_2} = {result}")

    number_1 = None
    number_2 = None
    op_selected = None


def forward_or_exit():
    global first_calculate
    global result
    global still_calculating
    forward_option = ""
    while still_calculating:
        if forward_option != "n" and forward_option != "c":
            print("Type [N] for a new calculus, or [E] to exit: ", end="")
        elif result and (forward_option == "c" or forward_option == "n"):
            print(
                f"Type [C] to continue with {result}, [N] for a new calculus, or [E] to exit: ", end="")

        forward_option = input().lower().strip()

        if forward_option == "n":
            calculator(result=None)
        elif (forward_option == "c") and result:
            calculator(result=result)
        elif forward_option == "e":
            print("Bye bye...")
            still_calculating = False
        else:
            print("Wrong option.")


def calculator(result):
    global op_selected
    ask_number(result)
    pick_an_operation()
    ask_number(result)
    perform_operation(op_selected)


forward_or_exit()
