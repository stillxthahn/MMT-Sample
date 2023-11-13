import socket

def readEmail(username, password, host, port):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  client.connect(server_address)

  #SERVER RESPONSE AFTER CONNECTION
  recv = client.recv(1024)
  recv = recv.decode()
  #print("May chu phan hoi sau khi ket noi:" + recv)

  if recv[:3] != '+OK':
      print('KHÔNG NHẬN ĐƯỢC PHẢN HỒI TỪ MÁY CHỦ !')
  else: print('KẾT NỐI ĐẾN MÁY CHỦ THÀNH CÔNG !')

  capaCommand = "CAPA\r\n"
  client.send(capaCommand.encode())
  recv1 = client.recv(1024)
  recv1 = recv1.decode()
  print(recv1)

  userCommand = f"USER {username}\r\n"
  client.send(userCommand.encode())
  recv2 = client.recv(1024)
  recv2 = recv2.decode()
  print(recv2)

  passCommand = f"PASS {password}\r\n"
  client.send(passCommand.encode())
  recv3 = client.recv(1024)
  recv3 = recv3.decode()
  print(recv3)

  statCommand = "STAT\r\n"
  client.send(statCommand.encode())
  recv4 = client.recv(1024)
  recv4 = recv4.decode()
  print(recv4)

  listCommand = "LIST\r\n"
  client.send(listCommand.encode())
  listData = client.recv(1024)
  listData = listData.decode()
  print(listData)

  uidlCommand = "UIDL\r\n"
  client.send(uidlCommand.encode())
  uidlData = client.recv(1024)
  uidlData = uidlData.decode()
  print(uidlData)

  choice = input("Bạn muốn đọc Email thứ mấy: ")
  retrCommand = f"RETR {choice}\r\n"
  print(retrCommand)
  client.send(retrCommand.encode())
  data = client.recv(1024)
  data = data.decode()
  print(f"Nội dung email của email thứ {choice}: ", data)
  client.close()



