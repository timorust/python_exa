def checkNumber(number):
	return number ** 3

def checkString(string):
	sum = ""
	for i in string:
		sum = 	sum + (i * 3)
	return sum


print(checkNumber(3))
print(checkString("abc"))
