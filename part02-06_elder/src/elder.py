# Write your solution here

print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))

print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))

if age1 > age2:
    olderPerson = name1
else:
    olderPerson = name2

if age1 != age2:
    print(f"The elder is {olderPerson}")
else:
    print(f"{name1} and {name2} are the same age")