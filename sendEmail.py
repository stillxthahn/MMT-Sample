import socket
import uuid
import time
def sendEmail(host, port, emailFrom):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  client.connect(server_address)

  #SERVER RESPONSE AFTER CONNECTION
  recv = client.recv(1024)
  recv = recv.decode()
  #print("May chu phan hoi sau khi ket noi:" + recv)

  if recv[:3] != '220':
      print('KHÔNG NHẬN ĐƯỢC PHẢN HỒI TỪ MÁY CHỦ !')
  else: print('KẾT NỐI ĐẾN MÁY CHỦ THÀNH CÔNG !')

  #EHLO COMMAND
  heloCommand = 'EHLO [' + host + ']\r\n'
  client.send(heloCommand.encode())
  recv1 = client.recv(1024)
  recv1 = recv1.decode()
  #print("Message after EHLO command:" + recv1)
  #if recv1[:3] != '250':
  #   print('250 reply not received from server.')

  #INPUT DATA
  print("Đây là thông tin soạn email: (nếu không điền vui lòng nhấn enter để bỏ qua)")
  TO = input('To: ')
  CC = input('CC: ')
  BCC = input('BCC: ')

  subject = input("Subject: ")
  content = input("Content: ")

  while True:
    attachFiles = input("Có gửi kèm file (1. có, 2. không): ")
    if (attachFiles == "1"):
      numberofFiles = input("Số lượng file muốn gửi: ")
      #for statement
      break
    elif (attachFiles == "2"): break;
    else: print("Lựa chọn không hợp lệ, bạn hãy nhập lại")
  mailFrom = f"MAIL FROM:<{emailFrom}>\r\n"
  client.send(mailFrom.encode())
  recv2 = client.recv(1024)
  recv2 = recv2.decode()
  #print("Message after MAIL FROM command:" + recv2)
  #if recv2[:3] != '250':
  #    print('250 reply not received from server.')

  rcptTo = f"RCPT TO:{TO}\r\n"
  client.send(rcptTo.encode())
  recv3 = client.recv(1024)
  recv3 = recv3.decode()
  #print("Message after RCPT TO command:" + recv3)
  #if recv3[:3] != '250':
  #    print('250 reply not received from server.')

  dataSend = 'DATA' + '\r\n'
  client.send(dataSend.encode())
  recv4 = client.recv(1024)
  recv4 = recv4.decode()
  #print("Message after RCPT TO command:" + recv4)

  # INPUTING DATA

 
  unique_id = uuid.uuid4()
  named_tuple = time.localtime()
  local_time = time.strftime("%a, %d %b %Y %H:%M:%S", named_tuple)

  MessageID = f"Message ID: {unique_id}@example.com\r\n"
  Date = f"Date: {local_time} +0700\r\n\r\n"
  To = f"To: {TO}\r\n"
  From = f"From: {emailFrom}\r\n"
  Subject = f"Subject: {subject}\r\n\r\n"
  Content = f"{content}\r\n"
  endMSG = ".\r\n"

  client.send(MessageID.encode())
  client.send(Date.encode())
  client.send(To.encode())
  client.send(From.encode())
  client.send(Subject.encode())
  client.send(Content.encode())
  client.send(endMSG.encode())

  recv5 = client.recv(1024)
  recv5 = recv5.decode()
  print("Đã gửi email thành công")
  client.close()
