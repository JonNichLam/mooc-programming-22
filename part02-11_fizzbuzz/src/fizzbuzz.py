# Write your solution here

number = int(input("Number:"))

outputString = ""

if number %3 == 0:
    outputString += "Fizz"
if number %5 == 0:
    outputString += "Buzz"

print(outputString)