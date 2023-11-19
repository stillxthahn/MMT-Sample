import socket
import uuid
import time
from body_format_attachment import body_format_attachment

def send_command(client, command):
  try:
    client.send(command.encode())
    response = client.recv(1024).decode()
    return response
  except Exception as e:
    print(f"Lỗi: {e}")
    return ""
def input_email(tos_list, ccs_list, bccs_list, subject, content, num_files, file_path):
  print("Đây là thông tin soạn email: (nếu không điền vui lòng nhấn enter để bỏ qua)")
  to_list_str = input("To: ")
  tos = to_list_str.split(", ")
  for to in tos:
    tos_list.append(to)
  cc_list_str = input("CC: ")
  ccs = cc_list_str.split(", ")
  for cc in ccs:
    ccs_list.append(cc)
  bcc_list_str = input("BCC: ")
  bccs = bcc_list_str.split(", ")
  for bcc in bccs:
    bccs_list.append(bcc)
  sub = input('Subject: ')
  subject.append(sub)
  subject = "".join(subject)
  con = input('Content: ')
  content.append(con)
  content = "".join(content)

  while True:
    attach_files = input("Có gửi kèm file (1. có, 2. không): ")
    if (attach_files == "1"):
      nums = input("Số lượng file muốn gửi: ")
      num_files.append(nums)
      num_files = "".join(num_files)
      num_files = int(num_files)
      for num in range(1, num_files + 1):
        attachment_path = input(f"Nhập đường dẫn file đính kèm cho file {num}: ")
        file_path.append(attachment_path)
      #"C:/Users/Admins/Downloads/img.jpg"
      #"C:/Users/lxtha/Desktop/ATTACHMENT.txt"
      #"C:/Users/lxtha/Downloads/ok.xls"
      #"C:/Users/lxtha/Downloads/unikey43RC5-200929-win64.zip"
      #send_attachment_file(client, "C:/Users/lxtha/Desktop/ATTACHMENT.txt")
      break
    elif (attach_files == "2"): break;
    else: print("Lựa chọn không hợp lệ, bạn hãy nhập lại")

def body_format(tos_list, ccs_list, username, emailFrom, subject, content):
    unique_id = uuid.uuid4()
    named_tuple = time.localtime()
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S", named_tuple)
    messageID = f"Message-ID: {unique_id}@example.com\r\n"
    date = f"Date: {local_time} +0700\r\n\r\n"
    to = f"To: {",".join(tos_list)}\r\n"
    cc = f"Cc: {",".join(ccs_list)}\r\n"
    from_ = f"From: {username} <{emailFrom}>\r\n"
    subject = f"Subject: {"".join(subject)}\r\n\r\n"
    content = f"{"".join(content)}\r\n"
    endMSG = ".\r\n"
    return messageID + date + to + cc + from_ + subject + content + endMSG


def sendEmail(username, emailFrom, host, port):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return
  tos_list = []
  ccs_list = []
  bccs_list = []
  subject = []
  content = []
  num_files = []
  file_path = []
  #SERVER RESPONSE AFTER CONNECTION
  send_command(client, f"EHLO [{host}]\r\n")
  send_command(client, f"MAIL FROM:<{emailFrom}>\r\n")
  input_email(tos_list, ccs_list, bccs_list, subject, content, num_files, file_path)
  for to in tos_list:
    send_command(client, f"RCPT TO:<{to}>\r\n")
  # for cc in ccs_list:
  #   send_command(client, f"RCPT TO:<{cc}>\r\n")
  send_command(client, f"DATA\r\n")
  # SENDING-DATA
  if (len(num_files) == 0  or int(num_files[0]) == 0):
    body = body_format(tos_list, ccs_list, username, emailFrom, subject, content)
    send_command(client, body)
  else:
    body_attachment = body_format_attachment(client, ",".join(tos_list), username, emailFrom, "".join(subject), "".join(content), num_files[0], file_path)
    client.send(body_attachment)
    send_command(client, "\r\n.\r\n")
  print("Đã gửi email thành công")
  client.close()

