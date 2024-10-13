# Transport Control Protocol (TCP) is one of the main protocols in the Transport layer of the Internet Protocol Suite.
# Its primary role is to facilitate communication between applications over a network, ensuring reliable data transfer.
# How TCP Works

#1. Three-Way Handshake:

# SYN: The client sends a SYN (synchronize) packet to the server to initiate a connection.
# SYN-ACK: The server responds with a SYN-ACK (synchronize-acknowledgment) packet.
# ACK: The client sends back an ACK (acknowledgment) packet, completing the handshake and establishing a connection.
#    Client                      Server
#      |                            |
#      |---- SYN ----------------->|
#      |                            |
#      |<---- SYN-ACK -------------|
#      |                            |
#      |---- ACK ----------------->|
#      |                            |
# Summary of Packets
# SYN: Used to initiate a connection.
# SYN-ACK: Acknowledges the SYN request and indicates the server is ready to establish a connection.
# ACK: Confirms the establishment of the connection.

#2. Data Transmission:

# After establishing the connection, data is sent in segments. Each segment is acknowledged by the receiver. 
# If an acknowledgment isn’t received within a specified time, TCP retransmits the segment.
#3. Connection Termination:

# When the communication is complete, TCP terminates the connection through a process that involves sending FIN (finish) packets, 
# ensuring both ends agree to close the connection.

# Use Cases
# TCP is widely used in applications where reliable communication is crucial, such as:

# Web Browsing (HTTP/HTTPS)
# Email (SMTP, IMAP, POP3)
# File Transfer (FTP)
# Remote Access (SSH, Telnet

# ---> Socket
# What is a Socket?
# A socket is an endpoint for sending or receiving data across a network.
# It provides the interface between an application and the network stack, allowing programs to communicate over a network.

# How Sockets Relate to TCP
# Connection Establishment:

# When using TCP, a socket is created on both the client and server sides.
# The TCP connection is established using the three-way handshake (as described previously),
# with sockets managing the underlying details of the connection.
# Data Transmission:

# After the connection is established, the application can send and receive data through the socket.
# The socket handles the segmentation and reassembly of data packets, allowing the application to work with a continuous stream of data.
# Socket Types:

# There are different types of sockets, but the two most common are:
# Stream Sockets (SOCK_STREAM): Used for TCP connections, providing a reliable, connection-oriented communication.
# Datagram Sockets (SOCK_DGRAM): Used for UDP connections, providing connectionless communication.
# Programming Interface:

# In programming languages like Python, Java, or C, the socket API allows developers to create, configure,
# and use sockets for network communication. This includes functions for binding, listening, accepting connections (for servers),
# connecting (for clients), sending, and receiving data.


#In Python, we communicate through servers through socket module available in Python-
# It requires three lines to create a socket and make a connection-
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('localhost', 8080))
#AF_INET(Address Family Internet Version 4) meaning telling the socket which typr of family address it will handle for communication.
#SOCK_STREAM is a type of socket that TCP will use.
# Stream Socket: This type of socket provides a reliable, two-way, connection-oriented communication channel.
# It is primarily used for TCP (Transmission Control Protocol) connections.
# socket.socket(): This function creates a new socket.
# socket.AF_INET: Specifies that the socket will use IPv4 addresses.
# socket.SOCK_STREAM: Indicates that the socket will use TCP (a stream socket).
#Here localhost is the server address, 8080 is the port number.

#Sending data and recieving response-
try:
    # Send data
    message = 'Hello, Server!'
    mysock.sendall(message.encode())
    
    # Receive a response
    response = mysock.recv(1024)
    print('Received:', response.decode())

finally:
    # Close the socket
    mysock.close()