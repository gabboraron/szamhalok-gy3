import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

connection.connect(server_address)

#values = (str(raw_input()))
values = "kerdes"
#packed_data = packer.pack(*values)

connection.sendall(values)
data = connection.recv(1024)
print data

connection.close()
