# Write your solution here
# Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.
#
# You may assume the input will be in lowercase entirely. Have a look at the examples below.

inputString = input("Please type in a string:")

vowelList = ['a', 'e', 'o']

for vowel in vowelList:
    if vowel in inputString:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")