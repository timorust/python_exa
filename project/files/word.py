words = open("word_lis.txt", "r+")
words.write("agent\nbeat\ncat\ndon\nearth\nfinal\nguest\nheight\nintro\njoint\n")
print(words.read())
words.close()