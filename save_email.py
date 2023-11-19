import os
from sendEmail import send_command
from read_json_file import read_json_file

def parse_email(data):
  lines = data.split('\n')
  content_type = ""
  boundary = ""
  mime_version = ""
  message_id = ""
  date = ""
  tos = []
  _from = ""
  subject = ""
  attachment_data = []
  in_attachment = False
  in_content = False
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
        data_attachment = ""
        file_name = ""
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          data_attachment = data_attachment + lines[k]
        attachment_data.append(data_attachment.strip())
    print("ID:", message_id, "Date:",date, "To:", tos, "From:",_from, "Subject:", subject, "Content:", content, "Attachment:", attachment_data)
    return {message_id, dates, tos, _from, subject, content, attachment_data}
    
def save_msg(data):
  data_arr = data.split('\r\n')
  json_filter = read_json_file("filter.json")
  
def save_email(client, list):
  for i in range(1, len(list) + 1):
      data = send_command(client, f"RETR {i}\r\n")
      save_msg(list[i])

      
#   #FILES = os.listdir(r"C:\Users\lxtha\Desktop\Mạng máy tính\MMT-Sample\local_mailbox")
#   # if (len(FILES) == 0):
#   #   print("DIRECTORY IS EMPTY")
#   # else: print(FILES)
