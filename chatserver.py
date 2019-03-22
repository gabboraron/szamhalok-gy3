import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
sock.bind(server_address)

sock.listen(1)
connection, client_address = sock.accept()
while True:
	data = connection.recv(1024)

	print data
	answ = str(raw_input())
	#reply = eval(answ)
	if (answ == "exit"):
		connection.close()
	connection.sendall(str(answ))
	#connection.close()
