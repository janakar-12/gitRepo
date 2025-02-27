import socket

HOST = "192.168.31.106"
PORT = 12345
filename = "test.txt"

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# send filename first
client_socket.send(filename.encode())

# open files and send contents
with open(filename, "rb") as file:
    while chunk := file.read(1024): # send 1024-byte chunks
        client_socket.send(chunk)

print(f"File {filename} sent successfully!")

# close socket
client_socket.close()