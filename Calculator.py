print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

#print (operations["*"] (4, 8))


def calculator():
    calculation = True
    num1 = float(input("What is the first number? : "))
    while calculation:
        for symbol in operations:
            print(symbol)
        operation_pick = input("Pick an operation from the above list: ")
        num2 = float(input("What is the second number? : "))
        answer = operations[operation_pick](num1, num2)
        print (f"{num1} {operation_pick} {num2} = {answer}")
        choice = input (f"Do you want to continue the operation? (Y/N)"
                        f"Type 'Y' to continue calculating with {answer}"
                        f"or type 'n' to start a new calculation.")

        if choice == "y":
            num1 = answer
        else:
            calculation = False
            print("\n" * 20)
            calculator()

calculator()
