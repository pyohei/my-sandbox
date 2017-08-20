#!/usr/bin/env ruby
require "socket"
require 'optparse'
require 'digest/sha1'

Version="0.0.1"
# ホストアドレス
host = "127.0.0.1"
# ポート番号
port = 3000
# 分割数
divide = 1

# 送信バッファサイズからシステムが使用するサイズを定義
SOCKETMANAGESIZE=16
IPHEADERSIZE=20
UDPHEADERSIZE=8

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
  if divide > 16
    divide = 16
  end
end

# ソケット(UDP)をオープンする
begin
  socket = UDPSocket.open()
  packet_size = socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF).int - SOCKETMANAGESIZE - IPHEADERSIZE - UDPHEADERSIZE
  puts "packet send buffer size: #{packet_size}byte"
rescue SocketError => e
  puts e.message
  exit(-4)
end

# ファイルの読み込み & ファイル分割
puts "reading file... " + filename
messages=[]
begin
  data = File.read(filename)
  len = (data.length / divide.to_f).ceil
  if len > packet_size
    len = packet_size
    divide = (data.length / len.to_f).ceil
  end
  divide.times do |i|
    messages << data[i*len,len]
  end
rescue => e
  puts e.message
  exit(-3)
end

# シーケンス制御用ダイジェスト
digest = Digest::SHA1.hexdigest(Time.now.to_s);

begin
  n = 0
  # 接続先アドレスとポートを指定しデータを送信(シーケンス制御用ヘッダー情報)
  socket.send(n.to_s + ":" + digest + ":" + messages.length.to_s, 0, host, port)
  puts "sending... host:#{host} port:#{port}"
  # 必ず最初に到達させたいパケットなのでスリープを入れている
  sleep 0.1
rescue SocketError => e
  puts e.message
  exit(-4)
end

begin
  threads = []
  n = 1
  m = messages.length
  # 分割数分繰り返す
  messages.each{|message|
    # スレッド作成
    # ソケット(UDP)をオープンする
    threads.push(Thread.new(n,m,UDPSocket.open(),message) {|n,m,socket,message|
      # 接続先アドレスとポートを指定しデータを送信
      _port = port + (n % 16)
      block = socket.send(n.to_s+":" + digest + ":" + message, 0, host, _port)
      puts "sending... #{n}/#{m} : #{message.length}byte port:#{_port}"
      # ソケットをクローズする
      puts "connection closed"
      socket.close
      })
    n += 1
  }

  # スレッドの終了を待つ
  threads.each {|t| t.join}
rescue => e
  puts e.message
end

exit(0)
