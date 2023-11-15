from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import mimetypes
def send_attachment_file(client, filepath):
  msg = MIMEMultipart()
  with open(filepath, 'rb') as attachment:
    attachment_part = MIMEApplication(attachment.read())
    attachment.close()
   
    attachment_part.set_type(str(type[0]), header='Content-Type',requote=True)
    attachment_part.add_header("Content-Disposition", "attachment")
    msg.attach(attachment_part)
  client.send(msg.as_bytes())

