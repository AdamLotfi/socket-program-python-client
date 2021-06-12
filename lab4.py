import socket

s = socket.socket(type=socket.SOCK_DGRAM)

port = 8888

s.connect(('192.168.56.102', port))

data = s.recvfrom(1024)

s.sendto(b'Hi, saya client. Terima Kasih!')

print (data)

s.close()
