import time
import socket
import matplotlib.pyplot as plt


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

# Initialize figure and plot
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Data from Raspberry Pi')
plt.show()

# Receive data and update plot
data_list = []
x_data = []

start = time.time()
while True:
    try:
        data = connection.recv(1024).decode()
        if not data:
            # No data received, break the loop
            break
        print('Received data:', data)

        # Convert data to numeric value and add it to the list
        try:
            value = float(data)
        except ValueError:
            # Ignore non-numeric values
            pass
        data_list.append(value)
        x_data.append(time.time() - start)  # x-axis data is the length of data_list

        # Update plot
        line.set_data(x_data, data_list)
        ax.relim()
        ax.autoscale_view()

        plt.draw()
        plt.pause(0.001)

    except ConnectionResetError:
        # Connection with Raspberry Pi reset, break the loop
        print('Connection with Raspberry Pi reset. Exiting...')
        break

# Close the connection
connection.close()