# Write your solution here
#Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

def squared(string, num):
    lenOfString = len(string)

    currentLetter = 0

    for x in range(num):
        currentString = ""

        for y in range(num):
            if currentLetter == lenOfString:
                currentLetter = 0
            currentString += string[currentLetter]

            currentLetter += 1

        print(currentString)

if __name__ == "__main__":
    squared('abd', 3)