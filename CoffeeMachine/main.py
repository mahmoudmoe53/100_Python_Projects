from art import *
from collections import Counter

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


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




while True:
    print(logo)

    coffee = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    ingredients = {

    }

    price = 0


    if coffee == "espresso":
        ingredients = MENU["espresso"]
        price += MENU["espresso"]["cost"]
    elif coffee == "latte":
        ingredients = MENU["latte"]
        price += MENU["latte"]["cost"]
    elif coffee == "cappuccino":
        ingredients = MENU["cappuccino"]
        price += MENU["cappuccino"]["cost"]
    elif coffee == "report":
        print(resources)
    elif coffee == "off":
        break

    print("Please insert coins")

    amount_of_quarters = float(input("How many quarters?\n"))
    amount_of_dimes = float(input("How many dimes?\n"))
    amount_of_nickels = float(input("How many nickels?\n"))
    amount_of_pennies = float(input("How many pennies?\n"))

    amount_inserted = (amount_of_quarters * QUARTER) + (amount_of_dimes * DIME) + (amount_of_nickels * NICKEL) + (amount_of_pennies * PENNY)

    change = amount_inserted - price

    if amount_inserted >= price:
        print(f"Here is your {coffee} ☕️, enjoy!")
        print(f"You have ${change} in change.")

    elif amount_inserted < price:
        print("Sorry that's not enough money. Money refunded.")

    another = input("Would you like to continue? Type 'Y' for yes or 'N' for no:\n").lower()


    if another == "y":
        print("\n" * 20)
    elif another == "n":
        print("Goodbye!")
        break
    elif another == "off":
        print("Goodbye!")
        break
    elif another == "report":
        print(resources)


