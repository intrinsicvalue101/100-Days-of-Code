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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0  # Set machine's profit


# TODO 1: Print report
# TODO 2: Check resources sufficient
def check_resources(drink):
    """Compare resources required in MENU to resources in the machine."""
    if drink == "espresso":
        water = MENU[drink]["ingredients"]["water"]
        coffee = MENU[drink]["ingredients"]["coffee"]

        if water > resources["water"]:
            return "Sorry there is not enough water."
        elif coffee > resources["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            return ""

    elif drink in ["latte", "cappuccino"]:
        water = MENU[drink]["ingredients"]["water"]
        coffee = MENU[drink]["ingredients"]["coffee"]
        milk = MENU[drink]["ingredients"]["milk"]

        if water > resources["water"]:
            return "Sorry there is not enough water."
        elif milk > resources["milk"]:
            return "Sorry there is not enough milk."
        elif coffee > resources["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            return ""


# TODO 3: Process coins
def process_coins(pennies, nickels, dimes, quarters):
    """Calculate total value of coins inserted."""
    q_value = quarters * 0.25
    d_value = dimes * 0.10
    n_value = nickels * 0.05
    p_value = pennies * 0.01

    total_value = q_value + d_value + n_value + p_value
    return total_value


# TODO 4: Check transaction successful
def is_transaction_successful(users_total, drink_price):
    """Check if payment is sufficient and update profit."""
    global profit

    if users_total < drink_price:
        return "Sorry that's not enough money. Money refunded."
    elif users_total > drink_price:
        change = round(users_total - drink_price, 3)
        profit += drink_price
        print(f"Here's ${change} in change.")
        return True
    else:
        profit += users_total
        return True


# TODO 5: Make coffee
def make_coffee(users_drink):
    """Deduct ingredients from resources and serve the drink."""
    if users_drink == "espresso":
        used = {
            "water": MENU[users_drink]["ingredients"]["water"],
            "coffee": MENU[users_drink]["ingredients"]["coffee"],
        }
        for key in used:
            resources[key] -= used[key]

    elif users_drink in ["latte", "cappuccino"]:
        water_required = MENU[users_drink]["ingredients"]["water"]
        coffee_required = MENU[users_drink]["ingredients"]["coffee"]
        milk_required = MENU[users_drink]["ingredients"]["milk"]

        resources["water"] -= water_required
        resources["coffee"] -= coffee_required
        resources["milk"] -= milk_required


def coffee_machine():
    """Main program loop for the coffee machine."""
    is_on = True

    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):\n")

        if user_choice in ["espresso", "latte", "cappuccino"]:
            resource_check = check_resources(drink=user_choice)

            if resource_check == "":
                print("Please insert coins.")
                user_quarters = float(input("How many quarters?: "))
                user_dimes = float(input("How many dimes?: "))
                user_nickels = float(input("How many nickels?: "))
                user_pennies = float(input("How many pennies?: "))

                users_total = process_coins(user_pennies, user_nickels, user_dimes, user_quarters)
                payment_processing = is_transaction_successful(users_total=users_total, drink_price=MENU[user_choice]["cost"])

                if payment_processing == True:
                    make_coffee(user_choice)
                    print(f"Here is your {user_choice}☕️. Enjoy!")
                else:
                    print(payment_processing)
            else:
                print(resource_check)

        elif user_choice == "report":
            print(
                f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: ${profit}"
            )

        elif user_choice == "off":
            is_on = False

        else:
            print("Sorry, that's not a valid choice. Please try again.")


coffee_machine()
