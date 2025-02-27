import socket

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the Raspberry Pi
client_socket.connect(("192.168.31.106", 12345))

# send data to server
client_socket.send("Hello, This is Dell!".encode())

# receive response from Raspberrypi
response = client_socket.recv(1024).decode()
print(f"Received from Server: {response}")

# close the connection
client_socket.close()