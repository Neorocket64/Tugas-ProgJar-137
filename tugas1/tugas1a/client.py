import sys
import socket
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = input("File yang dikirim: ")
fn, ext = os.path.splitext(Filename)

sock.send(Filename.encode('utf-8'))

try:
    # send file
    f = open (Filename, "rb")
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)
    else:
        f.close()
finally:
    sock.close()
    
f.close()
