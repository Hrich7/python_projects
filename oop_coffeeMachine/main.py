from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)