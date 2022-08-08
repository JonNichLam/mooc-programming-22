# Write your solution here
#Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

stringInput = input("Please type in a word:")
characterInput = input("Please type in a character:")
newString = stringInput
stringLen = len(newString)
while True:
    index = newString.find(characterInput)

    if index == -1:
        break

    if index + 3 <= stringLen:
        print(newString[index: index+3])
    newString = newString[index+1:]
    stringLen = len(newString)