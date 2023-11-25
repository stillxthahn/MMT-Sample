# THREADING
import socket
from readConfig import readConfig
import threading 
import time
from listreadEmail import listreadEmail
from get_email import get_email
from send_email import send_command
from send_email import send_command
from send_email import send_email
from read_email import read_email
once = False
choice = 0
data = readConfig()
USERNAME = data["Username"]
EMAIL = data["Email"]
PASSWORD = data["Password"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]
once = False
choice = 0

def thread_load_mail():
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (HOST, RECV_PORT)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return

  send_command(client, "CAPA\r\n")
  send_command(client, f"USER {EMAIL}\r\n")
  send_command(client, f"PASS {PASSWORD}\r\n")
  state = send_command(client, "STAT\r\n")

  listCommand = "LIST\r\n"
  list_data =  send_command(client, "LIST\r\n")

  uidl_data = send_command(client, "UIDL\r\n")
  list = listreadEmail(uidl_data)
  get_email(client, list)

def autoload_thread(choice, _time):
    while choice != 3:
        time.sleep(10)
        thread_load_mail()
        print("ALO")


autoload = threading.Thread(target=autoload_thread, daemon=True, args=(choice, int(AUTOLOAD)))

while True:
    print("Vui lòng chọn Menu:\r\n")
    print("1. Để gửi email\r\n")
    print("2. Để xem danh sách các email đã nhận\r\n")
    print("3. Thoát\r\n")
    choice = input("Bạn chọn: ")
    if (choice == "1"):
    #SEND EMAIL
        if (once == False):
            autoload.start()
            once = True
        send_email(USERNAME, EMAIL, HOST, SEND_PORT)
        #send_email(USERNAME, EMAIL, HOST, SEND_PORT)

    elif (choice == "2"):
    #READ EMAIL
        if (once == False):
            autoload.start()
            once = True
        read_email(EMAIL, PASSWORD, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)