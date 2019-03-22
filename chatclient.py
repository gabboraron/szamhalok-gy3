import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

connection.connect(server_address)

while True:
	values = (str(raw_input()))
	#values = "kerdes"
	#packed_data = packer.pack(*values)
	if (values == "exit"):
		connection.close()
		exit()
	connection.sendall(values)
	data = connection.recv(1024)
	print data