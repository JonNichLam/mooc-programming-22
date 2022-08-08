# Write your solution here
while True:
    stringInput = input("Please type in a string:")

    if stringInput == "":
        break

    print(stringInput)

    for x in range(len(stringInput)):
        print("-", end="")

    print("")