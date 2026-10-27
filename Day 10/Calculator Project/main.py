from operator import truediv

import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply, and divide.
def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

# TODO: Add these 4 functions into a dictionary as the values.
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# TODO: Use the dictionary operations to perform the calculations.
#print(operations["+"](4,8))
#print(operations["-"](4,8))
#operations["*"]
#operations["/"]

def calculator(number):
    #print("+\n-\n*\n/")
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    answer = operations[operation_symbol](number, num2)
    print(f"{number} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.").lower()

    if choice == "y":
        calculator(answer)
    else:
        return

start = True

while start:
    print(art.logo)
    firstnum = float(input("What's the first number? "))
    calculator(number=firstnum)