books = open("best sci-fi books.txt", "r")
booksFile = books.readlines()

for line in booksFile:
	# print(line)
	if "H.G. Wells" in line:
		print(line)

	




