# Write your solution here

inputString = input("Please type in a string:")

wordLength = len(inputString)

if inputString[1] == inputString[wordLength - 2]:
    print(f"The second and the second to last characters are {inputString[1]}")
else:
    print("The second and the second to last characters are different")