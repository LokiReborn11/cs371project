import socket


def client_connect():
  client_socket = socket.socket()
  port = 2048
  client_socket.connect(('127.0.0.1', port))
  print (client_socket.recv(1024).decode())
  client_socket.close()

if __name__ == '__main__':
    keepGoing = True
    while keepGoing:
      userinp = input("Input one of the following commands(CONNECT, UPLOAD, DOWNLOAD, DELETE, DIR, END):")
      if userinp == "CONNECT":
        client_connect()
      elif userinp == "END":
        keepGoing = False
        print("Goodbye!")
      else:
        print("Invalid command")

