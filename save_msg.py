import os
def save_msg():
  FILES = os.listdir(r"C:\Users\Admins\Desktop\Mạng máy tính\Tai_lieu_Socket\sample_code\Local\Inbox")
  if (len(FILES) == 0):
    print("DIRECTORY IS EMPTY")
  else: print(FILES)

save_msg()