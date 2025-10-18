def add (n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculate():
    should_accumulate = True
    num1 = float(input("What is your first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation: ')
        num2 = float(input("What is your second number? "))

        answer = operations[operation_symbol](num1, num2)

        print(f'{answer}')

        choice = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation.")

        if choice == 'yes':
            num1 = answer
        else:
            should_accumulate = False
            print(f"Your final result is: {answer}")

def main():
    try:
        calculate()
    except ValueError:
        print("Something went wrong!")

if __name__ == "__main__":
    main()