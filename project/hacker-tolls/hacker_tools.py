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
