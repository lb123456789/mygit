from socket import *

serverName = '127.0.0.1'
serverPort = 11000
BUFSIZ = 1024
ADDR = (serverName,serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)
i=1

while True:
    data = "client message"
    if not data:
        break
    clientSocket.send(data.encode('utf-8'))
    returnData = clientSocket.recv(BUFSIZ)
    if not returnData:
        break
    print('Return time is:%s' %returnData.decode('utf-8'))
    print(i)
    i=i+1
clientSocket.close()