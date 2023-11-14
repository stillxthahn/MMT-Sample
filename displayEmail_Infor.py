'''
#import socket
import extract_msg

def displayEmail_Infor(LIST):
    for i in LIST:
'''
import email
def displayEmail_Infor(List):
    for i in range(0, len(List)):
        PATH = f".\socket\debug\example@example.com\{List[i]}"
        email_File = open(PATH)
        #email_File = open(List[i])
        messagedic = email.Message(email_File)
        #content_type = messagedic["plain/text"]
        FROM = messagedic["From: "]
        TO = messagedic.getaddr("To: ")
        sujet = messagedic["Subject: "]
        email_File.close()
        print(str(i + 1) + ". " + FROM + ", " + sujet)
        #return content_type, FROM, TO, sujet
        #myMSG= read_MSG("client.msg")
        #print(myMSG)
    