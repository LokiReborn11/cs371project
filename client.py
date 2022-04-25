import os
import socket



IP = "localhost"
PORT = 2048
ADDR = (IP,PORT)
SIZE = 1024 ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"


def main():
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.connect(ADDR)
  while True:  ### multiple communications
      data = client.recv(SIZE).decode(FORMAT)
      cmd, msg = data.split("@")
      if cmd == "OK":
          print(f"{msg}")
      elif cmd == "DISCONNECTED":
          print(f"{msg}")
          break
        
      data = input("Input a command[UPLOAD(UPLOAD_filename), DOWNLOAD(DOWNLOAD_filename), DELETE(DELETE_filename), DIR, CLOSESERVER, DISCONNECT]> ")
      data2 = data 
      data = data.split("_")
      cmd = data[0]

      if cmd == "DISCONNECT":
        client.send(cmd.encode(FORMAT))

      elif cmd == "CLOSESERVER":
        client.send(cmd.encode(FORMAT))
        break

      elif cmd == "UPLOAD":
        client.send(data2.encode(FORMAT))
        file = open(data[1], "rb")
        sendData = file.read(1024)
        client.send(sendData)
        print("Data packet sent")
        file.close()
        print("File successfully sent")
       
      elif cmd == "DOWNLOAD":
        client.send(data2.encode(FORMAT))
        file = open(data[1], 'wb')
        recData = client.recv(SIZE)
        file.write(recData)
        print("Data packet received")
        file.close()

      elif cmd == "DELETE":
        client.send(data2.encode(FORMAT))
          
  print("Disconnected from the server.")
  client.close() ## close the connection

if __name__ == '__main__':
    main()
