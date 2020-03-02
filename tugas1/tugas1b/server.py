import sys
import socket
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port 31000, 31001, 31002
server_address = ('localhost', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)  # maks menerima 1 koneksi
i = 1  # file counter
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    # Receive the data in small chunks and retransmit it
    filename = ''
    while True:
        # data = connection.recv(32)
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"received {data}")
        filename += data
        if os.path.isfile(filename):
            print("Sending: " + filename)
            myfile = open(filename, "rb")
            connection.send(myfile.read())
        else:
            print("File not exist")
            connection.send("File not exist".encode())

    # Clean up the connection
    connection.close()
    print("success")
    # Clean up the connection
    connection.close()
socket.close()
