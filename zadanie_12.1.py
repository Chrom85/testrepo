import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adres = input('Podaj adres strony: ')
host = adres.split('/')
host=host[2]


mysock.connect((host, 80))

cmd = 'GET '+ adres+' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
