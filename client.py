import socket


def client_program():
  client_socket = socket.socket()
  port = 2048
  client_socket.connect(('127.0.0.1', port))
  print (client_socket.recv(1024).decode())
  client_socket.close()

if __name__ == '__main__':
    client_program()
