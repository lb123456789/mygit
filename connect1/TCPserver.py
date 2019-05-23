from socket import *
from time import ctime

host = ''
port = 11000
ADDR = (host, port)
BUFSIZ = 1024

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
#set the max number of tcp connection
tcpSocket.listen(5)

while True:
    print('waiting for connection...')
    clientSocket, clientAddr = tcpSocket.accept()
    print('conneted form: %s' %clientAddr[0])

    while True:
        try:
            data = clientSocket.recv(BUFSIZ)
        except IOError as e:
            print(e)
            clientSocket.close()
            break
        if not data:
            break
        returnData = "libin"+ctime()+data.decode('utf-8')
        clientSocket.send(returnData.encode('utf-8'))
    clientSocket.close()
tcpSocket.close()