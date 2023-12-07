import os 
import random

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


coinFlip()



