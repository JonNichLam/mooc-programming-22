# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
valueA = int(input("Value of a:"))
valueB = int(input("Value of b:"))
valueC = int(input("Value of c:"))

negSqrtValue = (-valueB - sqrt((valueB*valueB)-(4 * valueA*valueC)))/(2 * valueA)
posSqrtValue = (-valueB + sqrt((valueB*valueB)-(4 * valueA*valueC)))/(2 * valueA)

print(f"The roots are {posSqrtValue} and {negSqrtValue}")