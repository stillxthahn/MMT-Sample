import os
# def save_msg():
#   print("LIST FILE: ")
#   data = os.listdir(r"C:\Users\lxtha\Desktop\Mạng máy tính\socket\debug\example@example.com")
#   print(data)

# def parse_data_with_attachment(data):
#     lines = data.split('\n')
#     # content_type = next(line.split(": ", 1)[1] for line in lines if line.startswith("Content-Type"))
#     # boundary = content_type.split('boundary="')[1].strip('"')
#     # num_files = data.count(boundary) // 2
#     #mime_version = next(line.split(": ", 1)[1] for line in lines if line.startswith("MIME-Version"))
#     # message_id = next((line.split(": ", 1)[1] for line in lines if line.startswith("Message-ID")))
#     # date = next(line.split(": ", 1)[1] for line in lines if line.startswith("Date"))
#     # to = next(line.split(": ", 1)[1] for line in lines if line.startswith("To"))
#     # cc = next((line.split(": ", 1)[1] for line in lines if line.startswith("Cc")), None)
#     # _from = next(line.split(": ", 1)[1] for line in lines if line.startswith("From"))
#     # subject = next(line.split(": ", 1)[1] for line in lines if line.startswith("Subject"))
#     # json_object = {"status": "0", "date": date, "from": _from, "to": to, "subject": subject}
#     # print(message_id)
#     # print(json_object)

    

# data = """Message ID: 22dce494-9970-4137-ac2d-c897a8c7d25b@example.com
# Date: Sun, 19 Nov 2023 04:31:47 +0700

# To: example@example.com
# Cc: 
# From: Mang may tinh <example@example.com>
# Subject: NO FILE

# NO FILE

# """
# parse_data_with_attachment(data)

data = """Content-Type: multipart/mixed; boundary="------------mrM5nkpX3g7Cpl1orQFwlZJZ"
Message-ID: <77ce1dc5-2630-4a76-b527-64ca3fd8b2f6@fitus.edu.vn>
Date: Sun, 19 Nov 2023 05:00:09 +0700
MIME-Version: 1.0
User-Agent: Mozilla Thunderbird
Content-Language: vi-x-KieuCu.[Chuan]
To: example@example.com
From: =?UTF-8?Q?Xu=C3=A2n_Thanh?= <lxthanh22clc@fitus.edu.vn>
Subject: TEST THUNDERBIRD

This is a multi-part message in MIME format.
--------------mrM5nkpX3g7Cpl1orQFwlZJZ
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit

ALO

--------------mrM5nkpX3g7Cpl1orQFwlZJZ
Content-Type: text/plain; charset=UTF-8; name="ATTACHMENT.txt"
Content-Disposition: attachment; filename="ATTACHMENT.txt"
Content-Transfer-Encoding: base64

YWxvYWxv
--------------mrM5nkpX3g7Cpl1orQFwlZJZ
Content-Type: text/plain; charset=UTF-8; name="ATTACHMENT2.txt"
Content-Disposition: attachment; filename="ATTACHMENT2.txt"
Content-Transfer-Encoding: base64

eHhjdnhjdnh2Yw==

--------------mrM5nkpX3g7Cpl1orQFwlZJZ--"""
def parse_email(data):
  lines = data.split('\n')
  boundary = ""
  message_id = ""
  date = ""
  tos = []
  _from = ""
  subject = ""
  attachment_arr = []
  content = ""
  start_idx_attach = 0
  if (lines[0].startswith("Content-Type: multipart/mixed") == 1):
    boundary = lines[0][lines[0].find('"') + 1:len(lines[0]) - 1]
    for i in range(1, len(lines)):
      if lines[i].startswith("Message-ID"): message_id = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("Date"): date = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("To"): 
        to = lines[i].split(": ", 1)[1]
        tos = to.split(',')
      elif lines[i].startswith("From"): _from = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("Subject"): subject = (lines[i].split(": ", 1)[1]).strip()
      elif boundary in lines[i]:
        start_idx_attach = i
        break

    for j in range(start_idx_attach + 1, len(lines), 1):
      if lines[j].startswith("Content-Transfer-Encoding: 7bit"):
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          content = content + lines[k]
      elif lines[j].startswith("Content-Disposition: attachment"):
        attachment_data = ""
        file_name = lines[j][lines[j].find('"') + 1:len(lines[j]) + 1]
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          attachment_data = attachment_data + lines[k]
        attachment_data.strip()
        attachment = {"name": file_name, "data": attachment_data}
        attachment_arr.append(attachment)
    return {"ID": message_id, "date": date, "tos": tos, "from": _from, "subject": subject, "content": content, "attachment": attachment_arr}
  
data_parse = parse_email(data)
print(data_parse)