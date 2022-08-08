# Write your solution here
#Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

#Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.


inputString = input("Please type in a word:")
inputChar = input("Please type in a character:")

firstPos = inputString.find(inputChar)

inputStringLen = len(inputString)

if firstPos + 3 <= inputStringLen:
    print(inputString[firstPos:firstPos + 3])