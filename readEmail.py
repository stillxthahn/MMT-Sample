import socket
from listreadEmail import listreadEmail
from displayEmail_Infor import displayEmail_Infor
from load_email_json import load_email_json
from sendEmail import send_command
from get_email import get_email
#from save_msg import save_msg
def readEmail(username, password, host, port):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return
  #print("May chu phan hoi sau khi ket noi:" + recv)

  

  send_command(client, "CAPA\r\n")
  send_command(client, f"USER {username}\r\n")
  send_command(client, f"PASS {password}\r\n")
  send_command(client, "STAT\r\n")

  list_data =  send_command(client, "LIST\r\n")
  uidl_data = send_command(client, "UIDL\r\n")
  list = listreadEmail(uidl_data)
  print(list)
  get_email(client, list)

  choice = input("Bạn muốn đọc Email thứ mấy: ")
  retrCommand = f"RETR {choice}\r\n"
  client.send(retrCommand.encode())
  data = client.recv(1024)
  data = data.decode()
  print(f"Nội dung email của email thứ {choice}: ", data)
  

  client.close()
