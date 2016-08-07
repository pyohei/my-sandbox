#!/usr/bin/env ruby
require "socket"

socket = UDPSocket.open()

# ソケットの送信バッファサイズを取得する
bsize = socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF).int
puts "SO_SNFBUF: #{bsize} byte"

bsize = socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_RCVBUF).int
puts "SO_RCVBUF: #{bsize} byte"

# bsize = socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_SNDLOWAT).int
# puts "SO_SNDLOWAT: #{bsize} byte"

socket.close
