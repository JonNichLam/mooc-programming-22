# Write your solution here
cafeteriaCount = float(input("How many times a week do you eat at the student cafeteria?"))
priceOfStudentLunch = float(input("The price of a typical student lunch?"))
groceriesCostPerWeek = float(input("How much money do you spend on groceries in a week?"))

totalWeeklyCost = (cafeteriaCount * priceOfStudentLunch) + groceriesCostPerWeek
dailyCost = totalWeeklyCost /7
print("Average food expenditure:")
print(f"Daily: {dailyCost} euros")
print(f"Weekly: {totalWeeklyCost} euros")