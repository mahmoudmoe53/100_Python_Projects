from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from CoffeeMachine.art import logo

menu = Menu()

coffee = CoffeeMaker()

money = MoneyMachine()

while True:
    print(logo)
    choice = input(f"what would you like? {menu.get_items()}\n").lower()

    if choice == "latte" or choice == "cappuccino" or choice == "espresso":
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
    elif choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        print("Goodbye!")
        break


