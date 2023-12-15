from Hangman_screen import screenPic
from random import randint
wordsList = open("word_list.txt", "r")
wordsFile = wordsList.readlines()

def randWordList(list):
	for letter in list:
		randint(0, letter)

word = randWordList(wordsFile)
userChars = []
guessWord = len(word) * ["_"]
guessCount = 6


while True:
	guessChar = input("Enter a character").lower()
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
	if guessWord == word:
		print("win")
		break
	elif guessCount == 0:
		print("fail")
		break


	
		
# print(guessWord)
	# if guessChar not in userChars and 'a' <= guessChar <= 'z':
# Screen(0, "test", "test")

		

	