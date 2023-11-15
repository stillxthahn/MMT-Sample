import os
def save_msg(list):
  for path in list:
    try:
      f = open(path, 'r')
      text = f.read()
      print(text)
      f.close()
    except IOError:
      print("Problem reading: " + path)
