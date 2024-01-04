# client side
import socket

def requestWord():
	HOST = "127.0.0.1"
	PORT = 65432

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		# userQuery = input("Enter username please: => ").encode()
		s.sendall(b'query')
		wordList = s.recv(1024).decode('utf8')
	print(wordList)
	return wordList
