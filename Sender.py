import socket
import time

# Set up the server information
host = '192.168.226.27'  # Replace with the IP address of your PC
port = 5000

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the PC
sock.connect((host, port))
print('Connected to PC')

# Send continuous input data
while True:
    data = 'Data from Raspberry Pi: ' + str(time.time())  # Replace with your data collection logic
    sock.send(data.encode())
    time.sleep(1)  # Adjust the sleep duration as per your requirement
