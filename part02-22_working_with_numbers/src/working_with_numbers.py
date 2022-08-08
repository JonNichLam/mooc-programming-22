# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

inputCounter = 0
sum = 0
positiveNumbers = 0
negativeNumbers = 0

while True:
    inputNumber = int(input("Number:"))

    if inputNumber == 0:
        break

    inputCounter += 1
    sum += inputNumber
    mean = float(sum) / inputCounter

    if inputNumber > 0:
        positiveNumbers += 1
    else:
        negativeNumbers += 1


print(f"Numbers typed in {inputCounter}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positiveNumbers}")
print(f"Negative numbers {negativeNumbers}")