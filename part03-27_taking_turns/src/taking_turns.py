# Write your solution here
#Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

inputNum = int(input("Please type in a number:"))

num1 = 1
num2 = inputNum

while num1 <= num2:
    if num1 == num2:
        print(num1)
        break
    print(num1)
    print(num2)
    num1 += 1
    num2 -= 1