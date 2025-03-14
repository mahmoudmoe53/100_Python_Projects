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


profit = 0

while True:
    print(logo)

    coffee = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    machine_water = 300
    machine_coffee = 200
    machine_milk = 100

    price = 0


    if coffee == "espresso":
        if machine_water >= MENU["espresso"]["ingredients"]["water"] and machine_coffee >= MENU["espresso"]["ingredients"]["coffee"]:
            machine_water -= MENU["espresso"]["ingredients"]["water"]
            machine_coffee -= MENU["espresso"]["ingredients"]["coffee"]
            price += MENU["espresso"]["cost"]
            profit += MENU["espresso"]["cost"]
        else:
            print("Their is not enough resources to complete your order!")
            break
    elif coffee == "latte":
        if machine_water >= MENU["latte"]["ingredients"]["water"] and machine_coffee >= MENU["latte"]["ingredients"][
            "coffee"] and machine_milk >= MENU["latte"]["ingredients"]["milk"]:
            machine_water -= MENU["latte"]["ingredients"]["water"]
            machine_coffee -= MENU["latte"]["ingredients"]["coffee"]
            machine_milk -= MENU["latte"]["ingredients"]["milk"]
            price += MENU["latte"]["cost"]
            profit += MENU["latte"]["cost"]
        else:
            print("Their is not enough resources to complete your order!")
            break
    elif coffee == "cappuccino":
        if machine_water >= MENU["cappuccino"]["ingredients"]["water"] and machine_coffee >= MENU["cappuccino"]["ingredients"][
            "coffee"] and machine_milk >= MENU["cappuccino"]["ingredients"]["milk"]:
            machine_water -= MENU["cappuccino"]["ingredients"]["water"]
            machine_coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
            machine_milk -= MENU["cappuccino"]["ingredients"]["milk"]
            price += MENU["cappuccino"]["cost"]
            profit += MENU["cappuccino"]["cost"]
        else:
            print("Their is not enough resources to complete your order!")
            break
    elif coffee == "report":
        print(f"Water: {machine_water}")
        print(f"Milk {machine_milk}")
        print(f"Coffee: {machine_coffee}")
        print(f"Money: ${profit}")

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
        print(f"Water: {machine_water}")
        print(f"Milk {machine_milk}")
        print(f"Coffee: {machine_coffee}")
        print(f"Money: ${profit}")


