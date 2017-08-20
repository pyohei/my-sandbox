# -*- coding: utf-8 -*-
#
from __future__ import print_function
import sys
import socket
from contextlib import closing

def main():
  argv = sys.argv
  argc = len(argv)

  host = '127.0.0.1'
  port = 3000

  if argc == 3:
    port = int(argv[2])
    host = argv[1]
  elif argc == 2:
    host = argv[1]

  bufsize = 4096

  sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
  sock.bind((host, port))

  sys.stdout.write("input-> ")
  line = sys.stdin.readline()

  sock.sendto(line, (host, port))

  print(str(sock.recv(bufsize)))

  sock.close()

  return

if __name__ == '__main__':
  main()
