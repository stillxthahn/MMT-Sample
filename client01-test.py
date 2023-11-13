import socket
import time
import json
import uuid
with open('config.json') as f:
    data = json.load(f)
print(data)
rcptTo = 'RCPT TO:' + data['Gmail'] + '\r\n'
print(rcptTo)

HOST = "127.0.0.1"  # IP adress server
PORT = 2225        # port is used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print("Client connect to server with port: " + str(PORT))
client.connect(server_address)

recv = client.recv(1024)
recv = recv.decode()
print("May chu phan hoi sau khi ket noi:" + recv)

if recv[:3] != '220':
    print('Khong nhan duoc phan hoi ')

heloCommand = 'EHLO [' + HOST + ']\r\n'

client.send(heloCommand.encode())
recv1 = client.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

mailFrom = 'MAIL FROM:' + data['Gmail'] + '\r\n'
client.send(mailFrom.encode())
recv2 = client.recv(1024)
recv2 = recv2.decode()
print("Message after MAIL FROM command:" + recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

rcptTo = 'RCPT TO:' + data['Gmail'] + '\r\n'
print(rcptTo)
client.send(rcptTo.encode())
recv3 = client.recv(1024)
recv3 = recv3.decode()
print("Message after RCPT TO command:" + recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

dataSend = 'DATA' + '\r\n'
client.send(dataSend.encode())
recv4 = client.recv(1024)
recv4 = recv4.decode()
print("Message after RCPT TO command:" + recv4)

# START TO INPUT DATA
subject = input("Subject: ")
content = input("Content: ")
unique_id = uuid.uuid4()
named_tuple = time.localtime()
local_time = time.strftime("%a, %d %b %Y %H:%M:%S", named_tuple)
message = f"""Message ID: <{unique_id}@fitus.edu.vn>
Date: {local_time} +0700

To: lxthanh22clc@fitus.edu.vn
From: lxthanh22clc@fitus.edu.vn
Subject: {subject}

{content}
"""
message = message + '.\r\n'
client.send(message.encode())
quitCommand = 'QUIT'
client.send(quitCommand.encode())
recv2 = client.recv(1024)
recv2 = recv2.decode()
print("Message after QUIT command:" + recv2)

client.close()

