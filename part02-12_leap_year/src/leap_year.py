# Write your solution here

year = int(input("Please type in a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            boolInput = ""
        else:
            boolInput = "not "
    else:
        boolInput = ""
else:
    boolInput = "not "

print(f"That year is {boolInput}a leap year.")
