import socket

HOST = "192.168.31.106"
PORT = 12345

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send message
client_socket.send("Hello!, This is Windows!".encode())
#client_socket.send("server_socket.close()".encode())
data = client_socket.recv(1024).decode()
print(f"Received from Server: {data}")

client_socket.close()