from socket import *
import ctypes
import time

LockWorkStation = ctypes.windll.user32.LockWorkStation # The method that locks the OS imported from ctypes library

server_port = 9955

server_socket = socket(AF_INET, SOCK_STREAM) # The server socket that receives the TCP connection requests from the client: AF_INET is for IPv4, and SOCK_STREAM for TCP
server_socket.bind(('', server_port)) # Bind the server socket with this port
server_socket.listen(1) # Listen for at most one client request
print('The server is ready to receive TCP connection requests.')

while True:
    connection_socket, client_addr = server_socket.accept() # Accept the TCP connection request issued by the client, and create a new connection socket
    client_message = connection_socket.recv(1024).decode() # Receive the message from the client and encode it

    # Check for ID validity
    if client_message == '1210778' or client_message == '1210478' or client_message == '1212739':
        server_message = 'The OS will lock down after 10 seconds'
    else:
        server_message = 'Invalid ID'
    # Print the message on the server side and send it to the client
    print(server_message)
    connection_socket.send(server_message.encode())
    # Close the connection socket
    connection_socket.close()
    # Lock the OS after 10 sec
    if client_message == '1210778' or client_message == '1210478' or client_message == '1212739':
        time.sleep(10) # Sleep for 10 seconds
        LockWorkStation() # Lock the OS
