from Hangman_screen import screenPic
from clientHungman import requestWord

def gameHangman():
	wordList = requestWord()
	print(wordList)
	userChars = []
	guessWord = len(wordList) * ["_"]
	guessCount = 6


	while True:
		screenPic(guessCount, guessWord, userChars)
		guessChar = input("Enter a character: ").lower()
		if guessChar in userChars:
			print("You already guessed this letter. Try again.")
		elif guessChar not in "abcdefjklmnopqrstuvwxyz" :
			print("Please enter a letter a/z.")
		elif guessChar in wordList:
				for i in range(len(wordList)):
					if wordList[i] == guessChar:
						guessWord[i] = guessChar
						screenPic(guessCount, guessWord, userChars)
		elif guessChar not in userChars:
			userChars.append(guessChar)
			guessCount -= 1
			screenPic(guessCount, guessWord, userChars)
			# print(f"Number of attempts left: {guessCount}")

		if "".join(guessWord) == wordList:
			print("win")
			break
		elif guessCount == 0:
			print("fail")
			break


gameHangman()		

	