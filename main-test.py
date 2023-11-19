# import os
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

data = """Content-Type: multipart/mixed; boundary="===============7822051727812789830=="
MIME-Version: 1.0
Message-ID: f6b7af32-330f-46f9-84ea-f7e111915eac@example.com
Date: Mon, 20 Nov 2023 02:35:42 +0700
To: example@example.com
From: Mang may tinh <example@example.com>
Subject: TEST ZIP

--===============7822051727812789830==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

ALOALO
--===============7822051727812789830==
Content-Transfer-Encoding: base64
MIME-Version: 1.0
Content-Type: text/plain
Content-Disposition: attachment; filename="ATTACHMENT"

YWxvYWxv

--===============7822051727812789830==
Content-Transfer-Encoding: base64
MIME-Version: 1.0
Content-Type: application/x-zip-compressed
Content-Disposition: attachment; filename="unikey43RC5-200929-win64"

UEsDBBQAAgAIAKubTlFOW9b4k8YHAJhpEwAMAAAAVW5pS2V5TlQuZXhlzL17fBNl9jg8aZI20JZJ
gUhRkLiGtVrQatFtLdWEpjCFFIpcFZRqsaIiVkkEBbElLRCHgbqC8HVRWS+rLqzi6kIpqGkLbaFc
CqjcFKuiTi0uxQu03OZ3znlmkkwJu+/3975/vP0Q5pnncp7bOec55zzneSb/nkrOyHGcCX6KwnFV
HPtzcv/9z27guB4DqntwH3XbfU2VwbP7mvEzHp5tL3ny8YeevP8xe9H9s2Y97rU/8KD9Sd8s+8Oz
7O4x4+yPPT79wRsTE7s7VBgH7u1xftXQwve137VrX3j/L/R88f3r6Pnn95fBs9uat99/CZ7rHyh6
7zV6Tn9vAzzNDzz8HsaPrPvgffZ87/2V9FxH5VYNvf/9DdmY/8H31lH+B9/7hJ6vUf5VQ8/Q0/zA
AwTnroeLZmA7tD4W5HLc9EUWrmXk4mlaXDt3LRcf04PjbkmAgbJQ3G+zYjjOyobOgP9jGKJi1TLa
k2vuTYN9/eO9INleZh+txls5fSD0rgtyLdVWzoQVBHtxshECzT25jn/Cu9CLW31NON/agTw3Psqc
dUB8CjwLHTy3IjKhIIEr7cZxX262coVRyt3ofXCuF56OtATWIOy7SZ/HDmBvfHL6/d77OW7X8yaC
yS2F520JunxO+Hcjy8b1/jf0oQUA1sJLrbVrvuCNJSwj9RH6yn0Ez/KkS+A99vAs13gPxyVjRGUv
Gnsuo+el9T5U/PD02Rz3ZhwOEuTD6bs9Sj7vzNkY7ob/bVDhDbskX/DGJ2c/WQRhmguYE5oc96Xw
uP+f/glSYo2lJ9daDuO7C/4E/4kUQbJthzhIuiO+Jyff/Txlu2VwAif4t6W0PjwlhrLSX/p+SFqF
EJ7sbuC08on/gqGX7e1UsJtWMA0KqunZMESys48B0zsHqenWcPrKfEjnPJTeqqW33xOD74HJUJup
IZ4a4RwHJeyC1H/LXGix2CTPW2Hg0oOC5HGk8ZOCQsD8T0o4AKENEPqVf85ciTEB87vwkD2LDdxm
RDu5xwSAXhH0pkDSrLnU/eegZgDCJwEA8z1UKhlaYp/S+iA0RR76mSU8EOqfcxK0J01ocDvsFxVF


--===============7822051727812789830==--"""
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
parse_email(data)
