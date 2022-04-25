import socket
import os
import threading

IP = "localhost"
PORT = 2048
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_PATH = "server"

def server_program(conn, addr):
  serverConnect = True
  print(f"[NEW CONNECTION] {addr} connected.")
  conn.send("OK@Welcome to the server".encode(FORMAT))
  while serverConnect:
    data =  conn.recv(SIZE).decode(FORMAT)
    data = data.split("_")
    cmd = data[0]
    
    send_data = "OK@"
    if cmd == "CLOSESERVER":
      serverConnect = False
      #server_socket.close()
      print("Shutting server down")
      break
    elif cmd == "DISCONNECT":
      serverConnect = False
      conn.send("DISCONNECTED@Closing server connection".encode(FORMAT))
      break
    elif cmd == "UPLOAD":
      file = open(os.path.join("./serverStorage",data[1]), 'wb')
      recData = conn.recv(SIZE)
      file.write(recData)
      print("Data packet received")
      file.close()
      conn.send("OK@File successfully uploaded!".encode(FORMAT))
    elif cmd == "DOWNLOAD":
      file = open(os.path.join("./serverStorage",data[1]), 'rb')
      sendData = file.read(1024)
      conn.send(sendData)
      print("Data packet sent")
      file.close()
      print("File successfully sent")
      conn.send("OK@File successfully downloaded!".encode(FORMAT))

  print(f"{addr} disconnected")
  conn.close()
    

  
if __name__ == '__main__':
  print("Starting server")
  server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
  server_socket.bind(ADDR)
  server_socket.listen()
  print(f"server is listening on {IP}: {PORT}")
  while True:
    conn, addr = server_socket.accept() ### accept a connection from a client
    thread = threading.Thread(target = server_program, args = (conn, addr)) ## assigning a thread for each client
    thread.start()
