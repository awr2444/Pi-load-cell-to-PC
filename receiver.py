import socket
import math
# Set up the server information
host = ''  # Empty string means to listen on all available interfaces
port = 5000

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)
print('Waiting for Raspberry Pi connection...')

# Accept a connection
connection, address = sock.accept()
print('Connected by', address)

# Receive and print continuous data
while True:
    try:
        data = connection.recv(1024).decode()
        if not data:
            # No data received, break the loop
            break
        print('Received data:', data)
    except ConnectionResetError:
        # Connection with Raspberry Pi reset, break the loop
        print('Connection with Raspberry Pi reset. Exiting...')
        break

# Close the connection
connection.close()
