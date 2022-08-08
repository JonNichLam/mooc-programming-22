# Write your solution here

inputString = input("Please type in a sentence:")

variableString = inputString

while variableString.find(" ") != -1:
    print(variableString[0])

    spaceIndex = variableString.find(" ")

    variableString = variableString[spaceIndex +1:]

print(variableString[0])
