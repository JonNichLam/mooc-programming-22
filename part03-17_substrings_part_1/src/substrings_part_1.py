# Write your solution here
inputString = input("Please type in a string:")

lengthOfString = len(inputString)

for x in range(lengthOfString):
    print(inputString[0:x+1])