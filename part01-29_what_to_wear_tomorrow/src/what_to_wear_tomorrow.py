# Write your solution here

temperature = int(input("Temperature:"))
willItRain = input("Will it rain (yes/no):")

print("Wear jeans and a T-shirt")

if 20 >= temperature:
    print("I recommend a jumper as well")
if 10 >= temperature:
    print("Take a jacket with you")
if 5 >= temperature:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if willItRain == "yes":
    print("Don't forget your umbrella!")