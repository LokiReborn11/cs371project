import socket

def server_program():
  server_socket = socket.socket()  
  server_socket.bind(('', 2048))
  print("Socket created")
  server_socket.listen(5)

  while True:
    (client_socket, address) = server_socket.accept()
    print ('Got connection from ', address )
    client_socket.send('Thank you for connecting'.encode())
    client_socket.close()
    break
  
if __name__ == '__main__':
    server_program()
