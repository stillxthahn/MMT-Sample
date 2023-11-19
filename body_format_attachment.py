from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import uuid
import mimetypes
import time
import os
def body_format_attachment(client, to, username, emailfrom, subject, content, num_files, file_path):
  msg = MIMEMultipart()
  local_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
  msg['Message-ID'] = f"{uuid.uuid4()}@example.com"
  msg['Date'] = f"{local_time} +0700"
  msg['To'] = to
  msg['From'] = f"{username} <{emailfrom}>"
  msg['Subject'] = subject
  msg.attach(MIMEText(content, 'plain'))
  for path in file_path:
    with open(path, 'rb') as attachment:
      attachment_part = MIMEApplication(attachment.read())
      file_type = mimetypes.guess_type(path)
      file_name = os.path.basename(path)
      attachment_part.set_type(str(file_type[0]), header='Content-Type')
      attachment_part.add_header("Content-Disposition", "attachment", filename=os.path.splitext(file_name)[0])
      msg.attach(attachment_part)
  return msg.as_bytes()

