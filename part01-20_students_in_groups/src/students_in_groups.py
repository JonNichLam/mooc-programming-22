# Write your solution here
students = int(input("How many students on the course?"))
groupSize = int(input("Desired group size?"))

numberOfGroups = students/groupSize

if students%groupSize != 0:
    numberOfGroups += 1

print(f"Number of groups formed: {numberOfGroups}")