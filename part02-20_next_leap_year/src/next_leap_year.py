# Write your solution here

inputYear = int(input("Year:"))

leapYear = inputYear

while True:
    leapYear += 1

    if leapYear % 4 == 0:
        if leapYear % 100 ==0:
            if leapYear % 400 ==0:
                print(f"The next leap year after {inputYear} is {leapYear}")
                break
        else:
            print(f"The next leap year after {inputYear} is {leapYear}")
            break