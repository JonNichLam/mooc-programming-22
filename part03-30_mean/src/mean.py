# Write your code here
#Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.

def mean(num1, num2, num3):
    arithmeticMean = (num1 + num2 + num3)/ 3
    print(arithmeticMean)


#Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)