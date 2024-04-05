import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
"""
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}"""


symbol_of_operation = {
    '+' : lambda x, y : x + y,
    '-' : lambda x, y : x - y,
    '*' : lambda x, y : x * y,
    '/' : lambda x, y : x / y if y != 0 else 0,
    '**' : lambda x, y : x ** y,
    '%' : lambda x, y : x % y,

}


def calculator():
    os.system('clear')
    print(logo)
    first_number = float(input("What's the first number?: "))
    for ops in symbol_of_operation:
        print(ops)
    another_operation = 'y'
    while another_operation == 'y':
        operation = input("Pick an operation: ")
        if operation in symbol_of_operation:
            next_number = float(input("What's the next number?: "))
            if operation == '/' and next_number == 0:
                print('Error: Division by zero')
                answer = 0
            answer = symbol_of_operation[operation](first_number, next_number)
        
            print(f"{first_number} {operation} {next_number} = {answer}")
        
            another_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
            if another_operation == 'y':
                first_number = answer
            else:
                os.system('clear')
                calculator()
        else:
            print("Unsupported symbol of operation. Please enter one of the supported symbols")
            os.system('clear')
            calculator()


def main():
    calculator()

if __name__ == "__main__":
    main()