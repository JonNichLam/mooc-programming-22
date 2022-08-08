# Write your solution here

outputString = ""

inputString = input("Please type in a string:")

lenOfString = len(inputString)

numOfStars = 20 - lenOfString

for x in range(numOfStars):
    outputString += '*'

outputString += inputString

print(outputString)