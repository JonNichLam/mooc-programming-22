# Write your solution here

limitNum = int(input("Limit:"))

startingNum = 1
sumNum = 0

additionString = "The consecutive sum: "

while sumNum < limitNum:
    if sumNum + startingNum < limitNum:
        additionString += f"{startingNum} + "
    else:
        additionString += f"{startingNum} = "
    sumNum += startingNum
    startingNum +=1

additionString += f"{sumNum}"

print(additionString)