# Write your solution here

correctPin = 4321

attemptCounter = 0

while True:
    inputPin = int(input("PIN:"))

    attemptCounter += 1

    if inputPin == correctPin:
        if attemptCounter == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attemptCounter} attempts")
        break

    print("Wrong")