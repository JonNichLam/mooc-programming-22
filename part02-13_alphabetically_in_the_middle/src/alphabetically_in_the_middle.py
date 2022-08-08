# Write your solution here
firstLetter = input("1st letter:")
secondLetter = input("2nd letter:")
thirdLetter = input("3rd letter:")

letterList = [firstLetter]

if letterList[0] > secondLetter:
    letterList.append(firstLetter)
    letterList[0] = secondLetter
else:
    letterList.append(secondLetter)

if letterList[0] > thirdLetter:
    letterList.append(letterList[1])
    letterList[1] = letterList[0]
    letterList[0] = thirdLetter
else:
    if letterList[1] > thirdLetter:
        letterList.append(letterList[1])
        letterList[1] = thirdLetter
    else:
        letterList.append(thirdLetter)

print(f"The letter in the middle is {letterList[1]}")