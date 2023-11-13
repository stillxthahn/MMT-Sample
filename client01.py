from socket import *
import base64
import time

HOST = "127.0.0.1"  # IP adress server
PORT = 2225        # port is used by the server

mailserver = (HOST, PORT) #Fill in start #Fill in end
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'EHLO Alice\r\n'

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
quitCommand = 'QUIT'
clientSocket.send(quitCommand.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("Message after QUIT command:" + recv2)

clientSocket.close()