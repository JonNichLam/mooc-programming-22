# Write your solution here

word1 = input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")

if word1 < word2:
    alphabeticallyLastWord = word2
else:
    alphabeticallyLastWord = word1

if word1 != word2:
    print(alphabeticallyLastWord + "comes alphabetically last.")
else:
    print("You gave the same word twice.")