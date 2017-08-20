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
# 最大スレッド数
max_thread = 1

# UDPシーケンス制御用に追加するサイズ
SOCKETMANAGESIZE=80

# 引数チェック
begin
  params = ARGV.getopts('d','host:', 'port:', 'split:', 'thread:')
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

# スレッド数を指定されたか
if !params['thread'].nil?
  max_thread = params['thread'].to_i
  if max_thread > 16
    max_thread = 16
  end
end

# デバッグモード
debug = params['d']

# ソケット(UDP)をオープンする
begin
  socket = UDPSocket.open()
  # ソケットの送信バッファサイズを取得する
  bsize = socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF).int
  # UDPパケット最大サイズを超えてないか確認する
  if bsize > 65535
    bsize = 65535
  end
  if bsize < 65535
    socket.setsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF, 65535)
  end
  packet_size = bsize - SOCKETMANAGESIZE
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
#Process.getrlimit(:NOFILE)
begin
  n = 0
  # 接続先アドレスとポートを指定しデータを送信(シーケンス制御用ヘッダー情報)
  puts "sending... host:#{host} port:#{port}"
  socket.send(n.to_s + ":" + digest + ":" + messages.length.to_s, 0, host, port)
  # 必ず最初に到達させたいパケットなのでスリープを入れている
  sleep 0.1
rescue SocketError => e
  puts e.message
  exit(-4)
end

begin
  # 送信メッセージ作成
  messages.length.times {|i|
    messages[i] = i.to_s+":" + digest + ":" + messages[i]
  }

  threads = []
  mutex = Mutex::new

  m = messages.length

  # max_threadで指定した数だけスレッドを開始
  max_thread.times do |i|
    _port = port + i
    puts "create thread #{i}"
    threads << Thread.start { # スレッドを作成
      puts "connection open"
      socket = UDPSocket.open()
      loop do
        # messageをひとつ取り出し。競合回避のためにsynchronizeで囲う
        message = mutex.synchronize { messages.pop }
        # messageがなくなればループを終了
        break unless message
        # 接続先アドレスとポートを指定しデータを送信
        n,x = message.split(":",2) # 送信シーケンス番号を取得
        puts "sending... #{i}:#{n}/#{m} : #{message.length}byte port:#{_port}"
        block = socket.send(message, 0, host, _port)
        sleep 0.01 if debug
      end
      # ソケットをクローズする
      puts "connection closed"
      socket.close
    }
  end

  threads.each { |t| t.join }
rescue => e
  puts e.message
end

exit(0)
