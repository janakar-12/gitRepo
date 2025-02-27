import socket

HOST = "192.168.31.106"
PORT = 12345
filename = "test.txt"

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send(filename.encode())

with open(filename, "rb") as file:
    while chunk := file.read(1024):
        client_socket.send(chunk)

print(f"File {filename} transferred successfully!")

#info = client_socket.recv(1024).decode()
#cprint(info)

client_socket.close()