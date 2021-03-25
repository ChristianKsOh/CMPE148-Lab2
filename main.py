
#import socket module
from socket import *
import sys #In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a server socket
#FILL SOMETHING HERE
serverPort=6789
#serverHost='192.168.0.103'
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    #Establish the connectoin
    print('Ready to server...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)#FILL SOMETHING HERE
        filename = message.split()[1]
        f=open(filename[1:])
        outputdata = f.read()#fill something ehre
        #send one http header line into socket
        #FILL HERE
        okmessage ='\nHTTP/1.1 200 OK\n\n'
        connectionSocket.send(okmessage.encode())
        #connectionSocket.send(outputdata)
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #send response msesage for file not found
        #FILL SOMETHING HERE
        notfoundMessage ='\nHTTP/1.1 404 Not Found\n\n'
        connectionSocket.sendall(notfoundMessage.encode())
        connectionSocket.close()
        break
        #FILL SOMETHING HERE
    serverSocket.close()
    sys.exit()#Terimnate the program after sending the coressponding data

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
