#!/usr/bin/env ruby
#
require "socket"
require 'optparse'

Version="0.0.1"
# ホストアドレス
host = "127.0.0.1"
# ポート番号
port = 3000
# 分割数
divide = 1

# 引数チェック
begin
  params = ARGV.getopts('','host:', 'port:', 'split:')
rescue OptionParser::ParseError => e
  puts e.message
  exit(-1)
end

if ARGV.length < 1
  puts "ファイルを指定してください"
  exit(-2)
end

filename = ARGV[0]

# ホスト名（IPアドレス）が指定されたか
if !params['host'].nil?
  host = params['host']
end

# ポート番号が指定されたか
if !params['port'].nil?
  port = params['port'].to_i
end

# 分割数を指定されたか
if !params['split'].nil?
  divide = params['split'].to_i
end

# ファイルの読み込み & ファイル分割
puts "reading file... " + filename
messages=[]
begin
  data = IO.binread(filename)
  len = (data.length / divide).ceil
  divide.times do |i|
    messages << data[i*len,len]
  end
rescue => e
  puts e.message
  exit(-3)
end

puts "connecting... " + host + ":" + port.to_s
begin
  # ソケット(TCP)をオープンし接続先アドレスとポートを指定する（関数内部でsocket/connectを同時に実行している）
  socket = TCPSocket.open(host, port)
rescue SocketError => e
  puts e.message
  exit(-4)
end

begin
  n = 1
  m = messages.length
  # 分割数分繰り返す
  messages.each{|message|
    puts "sending... #{n}/#{m} : #{message.length}byte"
    # データを送信
    block = socket.write(message)
    n += 1
  }
rescue => e
  puts e.message
end

# ソケットをクローズする
socket.close
puts "connection closed"

exit(0)
