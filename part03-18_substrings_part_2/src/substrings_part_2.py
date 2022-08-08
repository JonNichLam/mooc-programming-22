# Write your solution here

inputString = input("Please type in a string:")

lenOfString = len(inputString)
for x in range(lenOfString):
    print(inputString[lenOfString - x- 1 : lenOfString])