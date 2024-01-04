# server side
import socket
import random

HOST = "127.0.0.1"
PORT = 65432


def randomWord():
	w = open("word_list.txt", "r")
	word = w.splitlines()
	randWord = random.choice(word)
	w.close()
	return randWord

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		print(f"Listening on port: => {PORT}")
		conn, addr = s.accept()
	with conn:
		print(f"Connecting to: => {addr}")
		data = conn.recv(1024)
		wordList = randomWord().encode()
		conn.sendall(wordList)