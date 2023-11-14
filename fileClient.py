# fileclient.py

import socket 
s = socket.socket()
s.connect(("localhost", 6767)) #lắng nghe ở cổng 6767

#Nhập vào tên file 
filename = input("Enter a filename ")

#Gửi tên file cho server
s.send(filename.encode())

#Nhận được dữ liệu từ server gửi tới
content = s.recv(1024)
print("CONTENT nhan dc khi chua decode: ", content)

print(content.decode())
s.close()