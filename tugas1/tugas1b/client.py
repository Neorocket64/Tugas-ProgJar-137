import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31002)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = input("File yang diminta: ")
fn, ext = os.path.splitext(Filename)

sock.send(Filename.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

try:
    # send file
    data = sock.recv(1024)
    newfile = fn + "_client" + ext
    f = open(newfile, 'wb')  # open in binary
    while (data):
        f.write(data)
        data = sock.recv(1024)
    else:
        f.close()
    print("File received with namefile "+newfile)
except:
    if data == b'File not exist':
        print("File not exist")
finally:
    sock.close()
    
f.close()
