from art import *
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 -n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculations():
    print(logo)

    calculator = True

    first_number = float(input("What is the first number?\n"))

    numb = 0

    numb += first_number

    while calculator:



        print('''
        +
        -
        *
        /
        ''')

        operator = input("Choose and operator\n")


        second_number = float(input("What is the second number?\n"))

        calculation = operations[operator](numb, second_number)

        print(f"{numb} {operator} {second_number} = {calculation}")

        cont = str(input(f"Type 'yes' to continue calculating with {calculation}, 'no' to start again or 'exit' to finish\n")).lower()

        if cont == "yes":
            numb = calculation
        elif cont == "exit":
            calculator = False
            print(goodbye)
        elif cont == "no":
            calculator = False
            print("\n" * 20)
            calculations()


calculations()