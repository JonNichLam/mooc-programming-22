# Write your solution here
widthInput = int(input("Width:"))
heightInput = int(input("Height:"))

hashLine = ""
for itter in range(widthInput):
    hashLine += "#"

for heightItter in range(heightInput):
    print(hashLine)