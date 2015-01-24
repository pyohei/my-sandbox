#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#client.py
import socket

# set partner's host and port
host = '127.0.0.1'
port = 3794

# setting of socket type
# (AF_INET...IPv4; SOCK_STREAM...using TCP/IP)
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set timeout (sec.)
#clientsock.settimeout(3)
clientsock.connect((host,port))

while True:
    print 'Type message...'

    # get message
    c_msg = raw_input()
    if c_msg == '':
      break
    print 'Wait...'

    # send message
    clientsock.sendall(c_msg)

    # recieve message
    rcvmsg = clientsock.recv(1024)
    print 'Received -> %s' % (rcvmsg)
    if rcvmsg == '':
      break

# close socket
clientsock.close()
