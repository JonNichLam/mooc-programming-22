# Write your solution here
farenheit = int(input("Please type in a temperature (F):"))
celsius = (farenheit - 32.0) * (5/9)

print(f"{farenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")
