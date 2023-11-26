# THREADING
import socket
from readConfig import readConfig
import threading 
from listreadEmail import listreadEmail
from get_email import get_email
from send_email import send_command
from send_email import send_command
from send_email import send_email
from read_email import read_email
from thread_load_email import thread_load_email
from read_json_file import read_json_file
once = False
choice = 0
data = read_json_file('config.json')
USERNAME = data["Username"]
EMAIL = data["Email"]
PASSWORD = data["Password"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]
once = False
choice = 0

autoload = threading.Thread(target=thread_load_email, daemon=True, args=(HOST, RECV_PORT, EMAIL, PASSWORD, choice, int(AUTOLOAD)))

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
    elif (choice == "2"):
    #READ EMAIL
        if (once == False):
            autoload.start()
            once = True
        read_email(EMAIL, PASSWORD, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)