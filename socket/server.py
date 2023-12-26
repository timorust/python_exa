# server side

import socket

HOST = "127.0.0.1"
PORT = 65432

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		print(f"Listening on port: => {PORT}")
		conn, addr = s.accept()
		with conn:
			print(f"Connecting to: => {addr}")
			data = conn.recv(1024)
			conn.sendall(data)