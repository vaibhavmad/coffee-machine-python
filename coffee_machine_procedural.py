machine_resources = {"water": 300.00, 'milk': 200.00, 'coffee': 100.00, 'money': 0.00}

coffee_details = {'espresso': {'water': 50,'coffee': 18,'milk': 0,'cost': 1.50},
    'latte': {'water': 200,'coffee': 24,'milk': 150,'cost': 2.50},
    'cappuccino': {'water': 250,'coffee': 24,'milk': 100,'cost': 3.00}}

coin_definition = {'pennies': 0.01,'nickles': 0.05,'dimes': 0.10,'quarters': 0.25}


def check_resource(coffee):
    if machine_resources['water'] >=coffee_details[coffee]['water'] and \
        machine_resources['milk'] >= coffee_details[coffee]['milk'] and \
        machine_resources['coffee'] >= coffee_details[coffee]['coffee']:
        return True
    else:
        return False


def update_resource(coffee):
    machine_resources['water'] = machine_resources['water'] - coffee_details[coffee]['water']
    machine_resources['milk'] = machine_resources['milk'] - coffee_details[coffee]['milk']
    machine_resources['coffee'] = machine_resources['coffee'] - coffee_details[coffee]['coffee']
    machine_resources['money'] += coffee_details[coffee]['cost']


def take_coins():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_amount = (coin_definition['quarters'] * quarters) + \
                   (coin_definition['dimes'] * dimes) + \
                   (coin_definition['nickles'] * nickles) + \
                   (coin_definition['pennies'] * pennies)
    return total_amount


def price_check(coffee, total_amount):
    if total_amount >= coffee_details[coffee]['cost']:
        return True
    else:
        return False


def calculate_return_change(coffee, total_amount):
    if total_amount > coffee_details[coffee]['cost']:
        change =  total_amount - coffee_details[coffee]['cost']
        return change


def serve_coffee(coffee):
    if check_resource(coffee):
        input_amount = take_coins()
        if price_check(coffee=coffee, total_amount=input_amount):
            change_amount = calculate_return_change(coffee=coffee, total_amount=input_amount)
            if change_amount:
                print(f"Here is ${round(change_amount, 2)} dollars in change")
            print(f"Here is your {coffee}. Enjoy!")
            update_resource(coffee)
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry, {coffee} is not available.")


while True:
    user_needs = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if user_needs == 'espresso':
        serve_coffee(user_needs)

    elif user_needs == 'latte':
        serve_coffee(user_needs)

    elif user_needs == 'cappuccino':
        serve_coffee(user_needs)

    elif user_needs == 'report':
        for key, value in machine_resources.items():
            print(f"{key}: {value}")

    elif user_needs == 'off':
        break

    else:
        print("That's an invalid response. Please try again.")
        continue