# Write your solution here

initialPassword = input("Password:")

while True:
    repeatPassword = input("Repeat password:")

    if repeatPassword == initialPassword:
        print("User account created!")
        break

    print("They do not match!")