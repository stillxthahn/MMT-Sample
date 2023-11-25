import os
import json
from read_json_file import read_json_file
from send_email import send_command
import re
def parse_data_with_attachment(data):
    lines = data.split('\n')
    content_type = next(line.split(": ", 1)[1] for line in lines if line.startswith("Content-Type"))
    boundary = content_type.split('boundary="')[1].strip('"')
    num_files = data.count(boundary) // 2
    mime_version = next(line.split(": ", 1)[1] for line in lines if line.startswith("MIME-Version"))
    message_id = next(line.split(": ", 1)[1] for line in lines if line.startswith("Message-ID"))
    date = next(line.split(": ", 1)[1] for line in lines if line.startswith("Date"))
    to = next(line.split(": ", 1)[1] for line in lines if line.startswith("To"))
    _from = next(line.split(": ", 1)[1] for line in lines if line.startswith("From"))
    subject = next(line.split(": ", 1)[1] for line in lines if line.startswith("Subject"))
    json_object = {"status": "0", "date": date, "from": _from, "to": to, "subject": subject, "filesattach": num_files}
    print(json_object)
def load_email_json(client, list):
    existing_data = read_json_file('Email_Infor.json')
    print(existing_data)
    start_index = 0
    if (len(existing_data) == 0):
        start_index = 1
    else: start_index = len(existing_data) + 1
    with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
        for i in range(start_index, len(list)):
            data = send_command(client, f"RETR {i}\r\n")
            if (data.find("multipart/mixed") != -1):
                parse_data_with_attachment(data_list)
            else:
                parse_data(data_list)
            CONTENT = ''
            TO = ''
            FROM = ''
            DATE = ''
            SUBJECT = ''
            index_Content = 0
            for j in range(0, len(data_list)):
                if index_Content == 0:
                    if data_list[j][0:2] == 'To':
                        TO = data_list[j][4:]
                    if data_list[j][0:4] == 'From':
                        FROM = data_list[j][6:]
                    if data_list[j][0:7] == 'Subject':
                        SUBJECT = data_list[j][9:]
                        index_Content = j
                        break
                    if data_list[j][0:4] == 'Date':
                        DATE = data_list[j][6:]
            for i in range(index_Content + 1, len(data_list) - 2):
                if data_list[i][0:7] == 'Content':
                    continue
                #if dataList[i] == '\r\n':
                    #continue
                CONTENT = CONTENT + data_list[i]
            data = {'status' : "0", 'date' : DATE, 'from' : FROM, 'to' : TO, 'subject' : SUBJECT, 'content' : CONTENT}
            existing_data.append(data)
        json.dump(existing_data, f)
        

# '''
# #import socket
# import extract_msg

# def displayEmail_Infor(LIST):
#     for i in LIST:
# '''
# import os
# import json
# from read_json_file import read_json_file
# def load_email_json(client, List):
#     feeds = []
    
#     print(existing_data_json)
#     print("JSON: ", existing_data_json)
#     with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
#         existing_data = existing_data.join(f.read())
#     print(existing_data)
    
#     with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
#         for i in range(1, len(List) + 1):
#             retrCommand = f"RETR {i}\r\n"
#             #print(retrCommand)
#             client.send(retrCommand.encode())
#             data = client.recv(1024)
#             data = data.decode()
#             dataList = data.split('\r\n')
#             CONTENT = ''
#             TO = ''
#             FROM = ''
#             DATE = ''
#             SUBJECT = ''
#             index_Content = 0
#             for j in range(0, len(dataList)):
#                 if index_Content == 0:
#                     if dataList[j][0:2] == 'To':
#                         TO = dataList[j][4:]
#                     if dataList[j][0:4] == 'From':
#                         FROM = dataList[j][6:]
#                     if dataList[j][0:7] == 'Subject':
#                         SUBJECT = dataList[j][9:]
#                         index_Content = j
#                         break
#                     if dataList[j][0:4] == 'Date':
#                         DATE = dataList[j][6:]
#             for i in range(index_Content + 1, len(dataList) - 2):
#                 if dataList[i][0:7] == 'Content':
#                     continue
#                 #if dataList[i] == '\r\n':
#                     #continue
#                 CONTENT = CONTENT + dataList[i]
#             data = {'status' : "0", 'date' : DATE, 'from' : FROM, 'to' : TO, 'subject' : SUBJECT, 'content' : CONTENT}
#         json.dump(feeds, f)
        