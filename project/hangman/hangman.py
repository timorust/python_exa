from Hangman_screen import screenPic
import random

wordsList = open("word_list.txt", "r")
wordsFile = wordsList.readlines()
word = random.choice(wordsFile)[:-1]

userChars = []
guessWord = len(word) * ["_"]
print(guessWord)
guessCount = 6


while True:
	screenPic(guessCount, guessWord, userChars)
	guessChar = input("Enter a character: ").lower()
	if guessChar in userChars:
		print("You already guessed this letter. Try again.")
	elif guessChar not in "abcdefjklmnopqrstuvwxyz" :
		print("Please enter a letter a/z.")
	elif guessChar in word:
			for i in range(len(word)):
				if word[i] == guessChar:
					guessWord[i] = guessChar
					screenPic(guessCount, guessWord, userChars)
	elif guessChar not in userChars:
		userChars.append(guessChar)
		guessCount -= 1
		screenPic(guessCount, guessWord, userChars)
	if "".join(guessWord) == word:
		print("win")
		break
	elif guessCount == 0:
		print("fail")
		break


		

	