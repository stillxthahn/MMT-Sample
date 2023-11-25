# import os
# # def save_msg():
# #   print("LIST FILE: ")
# #   data = os.listdir(r"C:\Users\lxtha\Desktop\Mạng máy tính\socket\debug\example@example.com")
# #   print(data)

# # def parse_data_with_attachment(data):
# #     lines = data.split('\n')
# #     # content_type = next(line.split(": ", 1)[1] for line in lines if line.startswith("Content-Type"))
# #     # boundary = content_type.split('boundary="')[1].strip('"')
# #     # num_files = data.count(boundary) // 2
# #     #mime_version = next(line.split(": ", 1)[1] for line in lines if line.startswith("MIME-Version"))
# #     # message_id = next((line.split(": ", 1)[1] for line in lines if line.startswith("Message-ID")))
# #     # date = next(line.split(": ", 1)[1] for line in lines if line.startswith("Date"))
# #     # to = next(line.split(": ", 1)[1] for line in lines if line.startswith("To"))
# #     # cc = next((line.split(": ", 1)[1] for line in lines if line.startswith("Cc")), None)
# #     # _from = next(line.split(": ", 1)[1] for line in lines if line.startswith("From"))
# #     # subject = next(line.split(": ", 1)[1] for line in lines if line.startswith("Subject"))
# #     # json_object = {"status": "0", "date": date, "from": _from, "to": to, "subject": subject}
# #     # print(message_id)
# #     # print(json_object)

    

# # data = """Message ID: 22dce494-9970-4137-ac2d-c897a8c7d25b@example.com
# # Date: Sun, 19 Nov 2023 04:31:47 +0700

# # To: example@example.com
# # Cc: 
# # From: Mang may tinh <example@example.com>
# # Subject: NO FILE

# # NO FILE

# # """
# # parse_data_with_attachment(data)

# # data ="""Message-ID: 83a8fe83-9818-4504-b39d-b3f4e6c1cfbe@example.com

# # Date: Thu, 23 Nov 2023 14:32:04 +0700

# # X-EsetId: 37303A297F03045A647162



# # To: example@example.com

# # Cc: 

# # From: Mang may tinh <example@example.com>

# # Subject: Thu Ta Minh



# # Thu Ta Minh

# # .

# # """

# # def parse_email(data):
# #   lines = data.split('\n')
# #   boundary = ""
# #   message_id = ""
# #   date = ""
# #   tos = []
# #   _from = ""
# #   subject = ""
# #   attachment_arr = []
# #   content = ""
# #   start_idx_attach = 0
# #   if (lines[0].startswith("Content-Type: multipart/mixed") == 1):
# #     boundary = lines[0][lines[0].find('"') + 1:len(lines[0]) - 1]
# #     for i in range(1, len(lines)):
# #       if lines[i].startswith("Message-ID"): message_id = lines[i].split(": ", 1)[1]
# #       elif lines[i].startswith("Date"): date = lines[i].split(": ", 1)[1]
# #       elif lines[i].startswith("To"): 
# #         to = lines[i].split(": ", 1)[1]
# #         tos = to.split(',')
# #       elif lines[i].startswith("From"): _from = lines[i].split(": ", 1)[1]
# #       elif lines[i].startswith("Subject"): subject = (lines[i].split(": ", 1)[1]).strip()
# #       elif boundary in lines[i]:
# #         start_idx_attach = i
# #         break

# #     for j in range(start_idx_attach + 1, len(lines), 1):
# #       if lines[j].startswith("Content-Transfer-Encoding: 7bit"):
# #         for k in range(j + 2, len(lines)):
# #           if boundary in lines[k]:
# #             break
# #           content = content + lines[k]
# #       elif lines[j].startswith("Content-Disposition: attachment"):
# #         attachment_data = ""
# #         file_name = lines[j][lines[j].find('"') + 1:len(lines[j]) + 1]
# #         for k in range(j + 2, len(lines)):
# #           if boundary in lines[k]:
# #             break
# #           attachment_data = attachment_data + lines[k]
# #         attachment_data.strip()
# #         attachment = {"name": file_name, "data": attachment_data}
# #         attachment_arr.append(attachment)
# #     return {"ID": message_id, "date": date, "tos": tos, "from": _from, "subject": subject, "content": content, "attachment": attachment_arr}
  
# # data_parse = parse_email(data)
# # print(type(data_parse))
# # print(data_parse)
# from readConfig import readConfig
# import threading 
# import time
# once = False
# choice = 0
# data = readConfig()
# USERNAME = data["Username"]
# EMAIL = data["Email"]
# PASSWORD = data["Password"]
# HOST = data["MailServer"]
# SEND_PORT = int(data["SMTP"])
# RECV_PORT = int(data["POP3"])
# AUTOLOAD = data["Autoload"]
# once = False
# choice = 0

# def autoload_thread(choice, _time):
#     counter = 0
#     while choice != 3:
#         time.sleep(1)
#         counter += 1
#         print(counter)
#         if (counter == _time): counter = 0


# autoload = threading.Thread(target=autoload_thread, daemon=True, args=(choice, int(AUTOLOAD)))

# while True:
#     print("Vui lòng chọn Menu:\r\n")
#     print("1. Để gửi email\r\n")
#     print("2. Để xem danh sách các email đã nhận\r\n")
#     print("3. Thoát\r\n")
#     choice = input("Bạn chọn: ")
#     if (choice == "1"):
#     #SEND EMAIL
#         if (once == False):
#             autoload.start()
#             once = True
#         #send_email(USERNAME, EMAIL, HOST, SEND_PORT)

#     elif (choice == "2"):
#     #READ EMAIL
#         if (once == False):
#             autoload.start()
#             once = True
#         #read_email(EMAIL, PASSWORD, HOST, RECV_PORT)

#     elif (choice == "3"):
#         exit(0)

# import os
# from get_email import parse_email
# file_path = os.path.join(os.getcwd(),"local_mailbox", "Inbox", "20231124231552865.msg")
# with open(file_path, "r") as f:
#   data = f.read()

# print(data)
# data_parse = parse_email(data, '\n\n')
# print(data_parse)

path = input()
print(path)
