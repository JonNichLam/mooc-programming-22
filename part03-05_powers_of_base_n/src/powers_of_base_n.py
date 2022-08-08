# Write your solution here
upperLimit = int(input("Upper limit:"))
base = int(input("Base:"))

startingNum = 1

while startingNum <= upperLimit:
    print(startingNum)
    startingNum *= base
