number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
operator = input("Enter the operator: ")

match operator:
    case '+':
        final_value = int(number_1) + int(number_2)
        print(final_value)
    case '-':
        final_value = int(number_1) - int(number_2)
        print(final_value)
    case '*':
        final_value = int(number_1) * int(number_2)
        print(final_value)
    case '/':
        final_value = int(number_1) / int(number_2)
        print(final_value)