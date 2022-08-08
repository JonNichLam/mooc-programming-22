# Write your solution here
limitNum = int(input("Limit:"))

startingNum = 1
totalNum = 0
while totalNum < limitNum:
    totalNum += startingNum
    startingNum += 1

print(totalNum)