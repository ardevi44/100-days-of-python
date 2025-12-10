MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25
}

machine_total_amount = 0
is_machine_on = True
current_drink_sale = 0


def print_menu(menu_list):
    print("Today we have:")
    count = 1
    for drink_name, info in menu_list.items():
        cost = info.get("cost")
        print(f"{count}. {drink_name.capitalize()} -> ${cost}")
        count += 1


def print_payment_allowed():
    global coins
    print("We only admit coins to pay our drinks\ncoins allowed:\n")
    for coin_name, value in coins.items():
        print(f"-> {coin_name.capitalize()}")


def show_report(data):
    print(f"""Water: {data["water"]}ml
Milk: {data["milk"]}ml
Coffee: {data["coffee"]}g
Money: ${machine_total_amount}
""")


def is_enough_resources_for_drink(drink):
    global MENU
    global resources
    # These are the ingredients of the selected drink by the user
    drink_ingredients = MENU[drink]["ingredients"]
    if "water" in drink_ingredients:
        if resources["water"] < drink_ingredients["water"]:
            return [False, "water"]
    if "coffee" in drink_ingredients:
        if resources["coffee"] < drink_ingredients["coffee"]:
            return [False, "coffee"]
    if "milk" in drink_ingredients:
        if resources["milk"] < drink_ingredients["milk"]:
            return [False, "milk"]
    return True


def add_amount(coins, value):
    global current_drink_sale
    current_drink_sale += coins * value
    print(f"This is the bill so far: {current_drink_sale}")


def is_total_reached(current_sale, drink_total):
    global current_drink_sale
    if current_drink_sale == drink_total or current_drink_sale > drink_total:
        return True
    return False


def subtract_resources(current_drink):
    global resources
    if "water" in current_drink["ingredients"]:
        resources["water"] -= current_drink["ingredients"]["water"]
    if "coffee" in current_drink["ingredients"]:
        resources["coffee"] -= current_drink["ingredients"]["coffee"]
    if "milk" in current_drink["ingredients"]:
        resources["milk"] -= current_drink["ingredients"]["milk"]


while is_machine_on:
    print_menu(MENU)
    user_choice = input("What would you like?: ").lower().strip()
    if user_choice == "off":
        print("Machine State: OFF")
        print("The coffee machine is off ...")
        is_machine_on = False
    elif user_choice == "report":
        show_report(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        resource_data = is_enough_resources_for_drink(user_choice)
        if isinstance(resource_data, list):
            resource_result = resource_data[0]
            missing_resource = resource_data[1]
            print(f"Sorry there is not enough {missing_resource}")
        else:
            current_drink = MENU[user_choice]
            drink_total = current_drink["cost"]
            print_payment_allowed()
            for coin_name, coin_value in coins.items():
                number_coins = int(
                    input(f"How many {coin_name.capitalize()}?: "))
                add_amount(number_coins, coin_value)
                if is_total_reached(current_drink_sale, drink_total):
                    break
            if current_drink_sale < drink_total:
                current_drink_sale = 0
                drink_total = 0
                print("Sorry that's not enough money. Money refunded")
            elif current_drink_sale == drink_total:
                machine_total_amount += current_drink_sale
                subtract_resources(current_drink)
                current_drink_sale = 0
                drink_total = 0
                print(f"Here is your {user_choice.capitalize()}. Enjoy!")
            elif current_drink_sale > drink_total:
                print(f"Here is {current_drink_sale - drink_total} in change")
                machine_total_amount += current_drink_sale - \
                    (current_drink_sale - drink_total)
                subtract_resources(current_drink)
                current_drink_sale = 0
                drink_total = 0
                print(f"Here is your {user_choice.capitalize()}. Enjoy!")
