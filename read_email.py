import socket
from listreadEmail import listreadEmail
from load_email_json import load_email_json
from send_email import send_command
from get_email import get_email
from Recv_list import output_receive_list
from Recv_list import read_chosen_file
from Recv_list import update_status
#from save_email import save_email

def get_list_emails(client, username, password):
  send_command(client, "CAPA\r\n")
  send_command(client, f"USER {username}\r\n")
  send_command(client, f"PASS {password}\r\n")
  send_command(client, "STAT\r\n")
  send_command(client, "LIST\r\n")
  uidl_data = send_command(client, "UIDL\r\n")
  list = listreadEmail(uidl_data)
  return list

def read_email(username, password, host, port):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return

  list = get_list_emails(client, username, password)
  get_email(client, list)

  print("Đây là danh sách các folder trong mailbox của bạn: \r\n 1. Inbox \r\n 2. Project\r\n 3. Important \r\n 4. Work \r\n 5. Spam")
  folder = input("Bạn muốn xem email trong folder nào: ")
  if (folder == '1'):
    print("Bạn chọn thư mục Inbox")
    output_receive_list("Inbox")
    choice = input("Bạn muốn đọc Email thứ mấy: ")
    read_chosen_file("Inbox", choice)
    update_status("Inbox", choice)

  elif (folder == '2'):
    print("Bạn chọn thư mục Project")
    output_receive_list("Project")
    choice = input("Bạn muốn đọc Email thứ mấy: ")
    read_chosen_file("Project", choice)
    update_status("Project", choice)
  elif (folder == '3'):
    print("Bạn chọn thư mục Important")
    output_receive_list("Important")
    choice = input("Bạn muốn đọc Email thứ mấy: ")
    read_chosen_file("Important", choice)
    update_status("Important", choice)
  elif (folder == '4'):
    output_receive_list("Work")
    choice = input("Bạn muốn đọc Email thứ mấy: ")
    read_chosen_file("Work", choice)
    update_status("Work", choice)
  elif (folder == '5'):
    output_receive_list("Spam")
    choice = input("Bạn muốn đọc Email thứ mấy: ")
    read_chosen_file("Spam", choice)
    update_status("Spam", choice)
