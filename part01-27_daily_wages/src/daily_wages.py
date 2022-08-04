# Write your solution here

hourlyWage = float(input("Hourly wage:"))
hoursWorked = int(input("Hours worked:"))
dayOfTheWeek = input("Day of the week:")

dailyWages = 0

if dayOfTheWeek == "Sunday":
    hourlyWage *= 2

dailyWages = hourlyWage * hoursWorked
print(f"Daily wages: {dailyWages} euros")
