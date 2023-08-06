# TODO 1.1: Menu

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# TODO 1.2: Resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 3: Check resources
def check_ingredients(order):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    water_order = menu[order]["ingredients"]["water"]
    milk_order = menu[order]["ingredients"]["milk"]
    coffee_order = menu[order]["ingredients"]["coffee"]

    if water >= water_order and milk >= milk_order and coffee >= coffee_order:
        return True
    else:
        return False


# TODO 4: Print price
def print_price(order):
    price = menu[order]["cost"]
    print(f"{order.title()} is £{price:.2f}.")


# TODO 5: Take money and decide if enough
def count_money(order):
    money = float(input("Please enter coins to the slot: £"))
    price = menu[order]["cost"]
    if money >= price:
        print("Thank you!")
        change = money - price
        print(f"Please, take your change: £{change:.2f}")
        # TODO 6: Give back a change
        return True
    else:
        return False


# TODO 7: Make a coffe
def make_coffee(order):
    print(f"Preparing...\nEnjoy your {order}.")


# TODO 7.1: Subtract from resources
def subtract_from_resources(order):
    global resources

    water_order = menu[order]["ingredients"]["water"]
    milk_order = menu[order]["ingredients"]["milk"]
    coffee_order = menu[order]["ingredients"]["coffee"]

    resources["water"] -= water_order
    resources["milk"] -= milk_order
    resources["coffee"] -= coffee_order


# TODO 9: Secret code to check resources left
def check_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water:  {water}\nMilk:   {milk}\nCoffee: {coffee}")


# TODO 8: Loop for working machine
def turn_on():
    while True:
        # TODO 2: Choose coffe
        user_choice = input("What coffe would you like to order (espresso, latte, cappuccino)? ").lower()
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            if check_ingredients(user_choice):
                print_price(user_choice)
                if count_money(user_choice):
                    subtract_from_resources(user_choice)
                    make_coffee(user_choice)
                else:
                    # TODO 5.1: If no enough money, print information
                    print("Sorry, not enough money provided.")

            else:
                # TODO 3.1: If not enough resources, print information
                print("Sorry, not enough resources in the machine.")

        elif user_choice == "resources":
            check_resources()
        # TODO 10: Secret code to turn off
        elif user_choice == "turn off":
            print("Turning off...\nGoodbye!")
            break
        else:
            print("Wrong choice!")


turn_on()
