# Write your solution here

borderString = ""
borderLength = 30

for x in range(borderLength):
    borderString += "*"

inputString = input("Word:")

wordString = ""

spacesInWordString = borderLength - 2 - len(inputString)

leftSpaces = int(spacesInWordString/2)
rightSpaces = spacesInWordString - leftSpaces

wordString += "*"
for x in range(leftSpaces):
    wordString += " "

wordString += inputString

for y in range(rightSpaces):
    wordString += " "

wordString += "*"

print(borderString)
print(wordString)
print(borderString)
