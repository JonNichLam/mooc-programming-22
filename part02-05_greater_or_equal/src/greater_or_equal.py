# Write your solution here
firstNum = int(input("Please type in the first number:"))
secondNum = int(input("Please type in the another number:"))

if firstNum > secondNum:
    greaterNum = firstNum
else:
    greaterNum = secondNum

if firstNum != secondNum:
    print(f"The greater number was: {greaterNum}")
else:
    print("The numbers are equal!")