from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create main_menu object from Menu class
main_menu = Menu()

    # create main_machine object from CoffeeMaker class
main_machine = CoffeeMaker()

    # create main_money_collect object from MoneyMachine class
main_money_collect = MoneyMachine()

# variable to keep the machine on, till it is not turned off
is_machine_on = True

# machine functioning, keeps machine on, till is_machine_on is true
while is_machine_on:



    # ask user for choice of drink user wants to drink
    user_choice = input("What would you like? (espresso/latte/cappuccino/):").lower().strip()

    # if user asks for off, is_machine_on is turned false and program exits
    if user_choice == 'off':
        print('Turning Off..')
        is_machine_on = False

    # if user asks for report, report of current items in machine is printed
    elif user_choice == 'report':
        main_machine.report()
        main_money_collect.report()

    # if user asks for drink, we check if input is valid, then we follow the machine process
    elif user_choice in main_menu.get_items():
        drink = (main_menu.find_drink(user_choice))
        quantity_okay = main_machine.is_resource_sufficient(drink)
        if quantity_okay:
            if main_money_collect.make_payment(drink.cost):
                main_machine.make_coffee(drink)
    else:
        print("Invalid input, please try again.")
