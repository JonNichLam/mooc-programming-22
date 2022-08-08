# Write your solution here

value = int(input("Value of gift:"))

if value < 25000:
    lowerLimit = 100
    taxRate =.08
    lowerValue = 5000
elif value < 55000:
    lowerLimit = 1700
    taxRate = .1
    lowerValue = 25000
elif value < 200000:
    lowerLimit = 4700
    taxRate = .12
    lowerValue = 55000
elif value < 1000000:
    lowerLimit = 22100
    taxRate = .15
    lowerValue = 200000
elif value > 1000000:
    lowerLimit = 142100
    taxRate = .17
    lowerValue = 1000000

tax = lowerLimit + ((value - lowerValue) * taxRate)

if value < 5000:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")