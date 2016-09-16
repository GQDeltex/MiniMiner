import socket

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind(('', 5000))
sock1.listen(1)
client, address = sock1.accept()
while True:
    print client.recv(20)
