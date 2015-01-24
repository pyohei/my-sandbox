#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#server.py
import socket
host = '127.0.0.1'
port = 3794

# setting of socket type
# (AF_INET...IPv4; SOCK_STREAM...using TCP/IP)
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind socket with IPv4
serversock.bind((host,port))

# waint connection
serversock.listen(1)

print 'Waiting for connections...'

# get (socket_object, (IP, Port))
clientsock, client_address = serversock.accept()

# sender and reciever share same object.
# and this object has possiblities of socket connection!!!

while True:
    #rcvmsg = clientsock.recv(1024)
    rcvmsg = clientsock.recvfrom(1024)
    print rcvmsg
    #print 'Received -> %s' % (rcvmsg)
    if rcvmsg == '':
      break
    print 'Type message...'
    s_msg = raw_input()
    if s_msg == '':
      break
    print 'Wait...'

    clientsock.sendall(s_msg) 
clientsock.close()
