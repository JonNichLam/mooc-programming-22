# Write your solution here

sentence = ""
previousWord = ""
while True:
    wordInput = input("Please type in a word:")

    if wordInput == "end" or previousWord == wordInput:
        print(sentence)
        break

    sentence += wordInput + " "
    previousWord = wordInput