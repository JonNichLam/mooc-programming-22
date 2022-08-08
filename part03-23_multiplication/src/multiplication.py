# Write your solution here
#Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

inputNum = int(input("Please type in a number:"))

num1 = 1

while num1 <= inputNum:
    num2 = 1
    while num2 <= inputNum:
        product = num1 * num2
        print(f"{num1} x {num2} = {product}")
        num2 += 1
    num1 += 1
