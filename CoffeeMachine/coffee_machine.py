import os
from coffee_machine_data import MENU, logo, resources

def report(resources):
    print(f"Water:  {resources.get('water')}ml")
    print(f"Milk:   {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money:  ${resources.get('money', 0)}")

def check_resources(user_choice):
    """Returns True when order can be made, False if the ingredients are insufficient."""
    for item in MENU.get(user_choice)['ingredients']:
        menu_item = MENU.get(user_choice)['ingredients'][item]
        resource_item = resources[item]
        if menu_item > resource_item:
            print(f"Sorry there is not enough {item}")
            return False
        return True

def update_resources(water_used, coffee_used, milk_used, money):
    resources["water"] -= water_used
    resources["coffee"] -= coffee_used
    resources["milk"] -= milk_used
    resources['money'] = resources.get('money', 0) + money

def add_resources():
    pass

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarters_input = input("How many quarters?: ")
    dimes_input = input("How many dimes?: ")
    nickels_input = input("How many nickels?: ")
    pennies_input = input("How many pennies?: ")

    total = 0

    try:
        quarters = int(quarters_input)
        total += quarters * 0.25
    except ValueError:
        pass

    try:
        dimes = int(dimes_input)
        total += dimes * 0.1
    except ValueError:
        pass

    try:
        nickels = int(nickels_input)
        total += nickels * 0.05
    except ValueError:
        pass

    try:
        pennies = int(pennies_input)
        total += pennies * 0.01
    except ValueError:
        pass

    return round(total, 2)
    

running = True
while running:
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match user_choice:
        case 'report':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            report(resources)
        case 'off':
            running = False
        case 'espresso' | 'latte' | 'cappuccino':
            if check_resources(user_choice):
                payment = process_coins()
                cost = MENU.get(user_choice)['cost']

                if payment >= cost : 
                    water_used = MENU[user_choice]['ingredients'].get('water')
                    coffee_used = MENU[user_choice]['ingredients'].get('coffee')
                    milk_used = MENU[user_choice]['ingredients'].get('milk', 0)
                    update_resources(water_used, coffee_used, milk_used, cost)
                    if payment > cost:
                        print(f"Here is ${round(payment - cost, 2)} in change")
                    print(f"Here is your {user_choice} ☕ Enjoy!")
                else:
                    print(f"Sorry that's not enough money. {user_choice} costs {cost}. Money refunded")  
            else:
                check_resources(user_choice)
        case _:
            print(f"We currently don't have the '{user_choice}' drink")

 
        









