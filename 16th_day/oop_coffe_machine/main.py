from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cfm = CoffeeMaker()
money_mc = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cfm.report()
        money_mc.report()
    else:
        drink = menu.find_drink(choice)
        if cfm.is_resource_sufficient(drink):
            if money_mc.make_payment(drink.cost):
                cfm.make_coffee(drink)




