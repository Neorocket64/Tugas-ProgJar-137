import socket
import os

TARGET_IP = "10.151.253.199"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

namafile="bart.png"
ukuran = os.stat(namafile).st_size

try :
   fp = open('bart.png','rb')
   k = fp.read()
   terkirim=0
   for x in k:
      k_bytes = bytes([x])
      sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
      terkirim = terkirim + 1
      print(k_bytes,f"terkirim {terkirim} of {ukuran} ")
finally :
   sock.close()
print("success")
fp.close()