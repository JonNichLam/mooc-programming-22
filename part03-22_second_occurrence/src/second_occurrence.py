# Write your solution here
# Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

stringInput = input("Please type in a string:")
substringInput = input("Please type in a substring:")
lengthOfSubstring = len(substringInput)
firstIndex = stringInput.find(substringInput)

newString = stringInput[firstIndex+lengthOfSubstring:]

secondIndex = newString.find(substringInput)

if secondIndex != -1:
    print(f"The second occurrence of the substring is at index {secondIndex+firstIndex+lengthOfSubstring}.")
else:
    print("The substring does not occur twice in the string.")
