from socket import *

server_name = 'localhost' # The host is the same device running both server and client programs
server_port = 9955 

client_socket = socket(AF_INET, SOCK_STREAM) # Create a client socket: AF_INET is for IPv4, and SOCK_STREAM for TCP
client_socket.connect((server_name, server_port)) # Request a TCP connection to the server process specified with the given IP address and port number

message = input('Enter your ID number:') # Prompt the user to enter his/her ID number
client_socket.send(message.encode()) # Send the message to the server

new_message = client_socket.recv(2048) # Receive a message from the server

print('Server\'s message:', new_message.decode()) # Decode the message received from the server and print it

client_socket.close()


