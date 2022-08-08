# Write your solution here

inputWord = input("Please type in a string:")

pos = len(inputWord) -1

while pos >= 0:
    print(inputWord[pos])
    pos -= 1
