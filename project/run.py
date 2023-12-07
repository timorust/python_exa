import random
import os

def diceRoll():
	cube1 = random.randint(1,6)
	cube2 = random.randint(1,6)
	return cube1, cube2
os.system("cls")
c1,c2 = diceRoll()
print(c1,c2)


# res = random.randint(1, 10)
# print(res)