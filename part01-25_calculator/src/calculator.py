# Write your solution here
number1 = int(input("Number 1:"))
operationString = ""
outcome = 0
if number1 != "":
    number2 = int(input("Number 2:"))
    operation = input("Operation:")
    if operation == 'add':
        operationString = '+'
        outcome = number1 + number2
        print(f"{number1} {operationString} {number2} = {outcome}")
    elif operation == 'multiply':
        operationString = '*'
        outcome = number1 * number2
        print(f"{number1} {operationString} {number2} = {outcome}")
    elif operation == 'subtract':
        operationString = '-'
        outcome = number1 - number2
        print(f"{number1} {operationString} {number2} = {outcome}")
