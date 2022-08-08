from math import sqrt
# Write your solution here

while True:
    number = int(input("Please type in a number:"))

    if number == 0:
        print("Exiting...")
        break

    if number > 0:
        sqrtNumber = sqrt(number)

        print(sqrtNumber)
    else:
        print("Invalid number")