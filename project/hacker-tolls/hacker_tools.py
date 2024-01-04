import os 
import random


def convertTemp():
    userInput = input("Please enter a temperature between 32F <=> 100C : ")
    temp = float(userInput[:-1])
    unit = userInput[-1]
    if unit.upper() == 'F':
        result = (temp - 32) * 5/9
        print(f"{temp}Fahrenheit is: => {result:.2f}°Celsius")
    elif unit.upper() == 'C':
        result = (temp * 9/5) + 32
        print(f"{temp}° Celsius is: => {result:.2f} Fahrenheit")
    else:
        print("Invalid input. Please enter a number with a corresponding unit (32F or 100C).")
convertTemp()

def atBashCipher(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in message:
        if char.lower() in abc:
            encrypted += abc[len(abc) - 1 - abc.index(char.lower())]
        else:
            encrypted += char
    return encrypted
userInput = input("Enter a message: ")
result = atBashCipher(userInput)
print(f"The encrypted message is: => {result}")

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            if not is_upper:
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            result += char

    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)

def calculate_gematria(hebText):
    gymDict = {' ': 0, 'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}
    result = 0
    for char in hebText:
        result += gymDict[char]
    return result

while True:
    hebText = input("please enter heb text")
    result = calculate_gematria(hebText)
    print(f"Gematria is: => {result}")
    


def find_longest_unique_substring(string):
    resString = ""
    length = len(string)

    for i in range(length):
        for j in range(i, length):  
            subString = string[i:j + 1]
            if len(set(subString)) == len(subString) and len(subString) > len(resString):
                resString = subString

    return resString

result = find_longest_unique_substring("11221234")
print(result)


def coinFlip():
	stats = [0, 0]
	while True:

		ranNum = random.randint(0,1)
		print ("Head") if ranNum == 0 else print("Tail")
		stats[ranNum] +=1
		print(f"head: {stats[0]}\nTail: {stats[1]}")
		key =input("press enter to toss again, q to quite left...")
		if key == 'q':
			break
		os.system("cls")
	return stats

stats = [0, 0]
def coinFlipSimulation():
	while True:
		ranNum = random.randint(1,100)
		print(f"head: {stats[0]}\nTail: {stats[1]}")
		key =input("press enter to toss again, q to quite left...")
		if key == 'q':
			break
		os.system("cls")
		if ranNum <= 30:
			stats[0] +=1
		elif ranNum > 30: stats[1] +=1
	return stats

print(coinFlipSimulation())





