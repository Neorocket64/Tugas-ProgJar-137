import socket


SERVER_IP = '10.151.254.227'
SERVER_PORT = 5006
NAMAFILE='coba.png'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

fp = open(NAMAFILE,'wb+')
ditulis=0

counter=0
while True :
    data, addr = sock.recvfrom(1024)
    if not data :
        break
    counter=counter+len(data)
    print(addr," blok ", counter,"panjang : ",len(data), data)
    fp.write(data)
print("success")
fp.close()
