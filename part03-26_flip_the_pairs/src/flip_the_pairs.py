# Write your solution here

#Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

inputNum = int(input("Please type in a number:"))
x = 0
while x < int(inputNum/2):

    print((x+1) * 2)
    print(2*x + 1)

    x += 1

if inputNum % 2 == 1:
    print(inputNum)