# Write your solution here

while True:
    inputEditor = input("Editor")

    if inputEditor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif inputEditor.lower() == 'notepad' or inputEditor.lower() == 'word':
        print("awful")
    else:
        print("not good")